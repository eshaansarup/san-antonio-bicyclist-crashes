"""Build intersection-to-intersection-style crash segments from city centerlines.

This uses the City of San Antonio Street Centerlines service. The service's
segments are the closest reproducible equivalent to the City's Vision Zero
"from street/to street" areas. CRIS crashes are joined to the nearest road
centerline segment and summarized separately for 2016-2025 and partial 2026.
"""

from pathlib import Path

import geopandas as gpd
import pandas as pd
import requests


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw" / "myexport_final.csv"
OUT = ROOT / "outputs"
DATA = ROOT / "data" / "boundaries"
OUT.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

SERVICE = (
    "https://services.arcgis.com/tNJpAOha4mODLkXz/arcgis/rest/services/"
    "Transportation/FeatureServer/0/query"
)


def download_centerlines():
    """Download the official centerline layer in pages as GeoJSON."""
    features = []
    offset = 0
    fields = (
        "segmentid,streetid,fullname,name,street_class,shape__length,"
        "lfrom,lto,rfrom,rto"
    )
    while True:
        params = {
            "where": "street_class NOT IN (5, 13, 16)",
            "outFields": fields,
            "returnGeometry": "true",
            "outSR": "4326",
            "f": "geojson",
            "resultOffset": offset,
            "resultRecordCount": 1000,
        }
        response = requests.get(SERVICE, params=params, timeout=120)
        response.raise_for_status()
        page = response.json()
        page_features = page.get("features", [])
        features.extend(page_features)
        if len(page_features) < 1000:
            break
        offset += len(page_features)
    return gpd.GeoDataFrame.from_features(features, crs="EPSG:4326")


def load_crashes():
    raw = pd.read_csv(RAW, skiprows=12, low_memory=False)
    severity = {"K - FATAL INJURY", "A - SUSPECTED SERIOUS INJURY"}
    people = raw[
        (raw["City"] == "SAN ANTONIO")
        & (raw["Person Type"] == "3 - PEDALCYCLIST")
        & raw["Person Injury Severity"].isin(severity)
    ].copy()
    people["death"] = (
        people["Person Injury Severity"] == "K - FATAL INJURY"
    ).astype(int)
    people["serious_injury"] = (
        people["Person Injury Severity"] == "A - SUSPECTED SERIOUS INJURY"
    ).astype(int)
    people["Latitude"] = pd.to_numeric(people["Latitude"], errors="coerce")
    people["Longitude"] = pd.to_numeric(people["Longitude"], errors="coerce")
    crashes = (
        people.groupby("Crash ID", as_index=False)
        .agg(
            year=("Crash Year", "first"),
            latitude=("Latitude", "first"),
            longitude=("Longitude", "first"),
            deaths=("death", "sum"),
            serious_injuries=("serious_injury", "sum"),
        )
        .dropna(subset=["latitude", "longitude"])
    )
    return gpd.GeoDataFrame(
        crashes,
        geometry=gpd.points_from_xy(crashes.longitude, crashes.latitude),
        crs="EPSG:4326",
    )


def main():
    roads = download_centerlines()
    crashes = load_crashes()
    roads_projected = roads.to_crs(2278)
    crashes_projected = crashes.to_crs(2278)
    joined = gpd.sjoin_nearest(
        crashes_projected,
        roads_projected[
            [
                "segmentid",
                "fullname",
                "name",
                "street_class",
                "lfrom",
                "lto",
                "rfrom",
                "rto",
                "geometry",
            ]
        ],
        how="left",
        distance_col="match_distance_ft",
    )
    joined["match_distance_ft"] = joined["match_distance_ft"].round(1)
    joined["road_label"] = (joined["fullname"].astype("string")
                             .fillna(joined["name"].astype("string")))
    joined["year"] = pd.to_numeric(joined["year"], errors="coerce")

    road_lengths = roads_projected[["segmentid", "geometry"]].copy()
    road_lengths["length_miles"] = road_lengths.geometry.length / 5280
    road_lengths = road_lengths.drop(columns="geometry")
    joined = joined.merge(road_lengths, on="segmentid", how="left")

    for label, mask in {
        "2016_2025": joined["year"].between(2016, 2025),
        "2026_partial": joined["year"].eq(2026),
    }.items():
        summary = (
            joined[mask & joined["segmentid"].notna()]
            .groupby(
                [
                    "segmentid",
                    "road_label",
                    "street_class",
                    "lfrom",
                    "lto",
                    "rfrom",
                    "rto",
                    "length_miles",
                ],
                dropna=False,
                as_index=False,
            )
            .agg(
                crashes=("Crash ID", "nunique"),
                deaths=("deaths", "sum"),
                serious_injuries=("serious_injuries", "sum"),
                first_year=("year", "min"),
                last_year=("year", "max"),
                max_match_distance_ft=("match_distance_ft", "max"),
            )
            .sort_values(["crashes", "deaths"], ascending=False)
        )
        summary.insert(
            1,
            "interpretation",
            "CRIS crashes joined to an official city centerline segment; raw count",
        )
        summary.to_csv(OUT / f"centerline_segments_{label}.csv", index=False)

    joined.drop(columns="geometry").to_csv(
        OUT / "crashes_with_centerline_segments.csv", index=False
    )
    print("2016-2025 top centerline segments")
    print(
        pd.read_csv(OUT / "centerline_segments_2016_2025.csv")
        .head(20)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
