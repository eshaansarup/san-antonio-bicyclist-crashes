# San Antonio bicyclist crash analysis

Analysis of Texas CRIS records for pedalcyclists killed or suspected seriously injured in crashes.

The main reporting window is **2024 through Sept. 1, 2026**. We chose it as a follow-up to the City of San Antonio's Bicycle High Injury Network dashboard:

[City of San Antonio Bicycle High Injury Network dashboard](https://cosagis.maps.arcgis.com/apps/dashboards/4f93c195971a44d28e6e5b069d673c38)

Treat 2024 through Sept. 1, 2026 as one reporting period. The CRIS export includes 2026 records through the latest available date.

## Notebooks to run

### 1. Main analysis

`san_antonio_bicyclist_crashes.ipynb`

Run this first. It creates the main story tables:

- San Antonio deaths and serious injuries by year;
- Texas city comparison rates for the current reporting window;
- bicycle-commute comparisons;
- Census tract hotspots;
- City Council district totals;
- victim characteristics, helmet status and police-recorded contributing factors; and
- comparison with the City's official HIN corridors.

The notebook uses the Census API for current Texas-city population and bicycle-commute data. It may require a Census API key; enter it in the clearly labeled cell when prompted.

### 2. Current corridor map

`candidate_corridors_victim_map_no_hin.ipynb`

Run this after the main analysis. It uses the local CRIS and Streets files to identify repeat-crash roadway stretches from 2024 through Sept. 1, 2026.

It does **not** call or filter against the City's official HIN API. It creates:

- `outputs/candidate_corridors_2024_2026.csv`
- `outputs/candidate_corridors_victim_map_2024_2026.html`

The HTML map includes street context, highlighted candidate corridors, clickable crash points, deaths versus serious injuries, victim age and gender, helmet status, police-recorded contributing factors and coordinates.

These are exploratory candidate corridors, not an official City ranking.

### Legacy notebook — ignore for current work

`publish_datawrapper_charts.ipynb`

This was used to initiate the Datawrapper charts. The new charts have different titles and subtitles. It is not part of the current run order.

## Data files

### Required raw inputs

- `data/raw/myexport_final.csv` — TxDOT CRIS export used by both analysis notebooks.
- `data/raw/Streets.zip` — San Antonio street centerline layer used by the corridor map.
- `data/population_estimates.csv` — historical San Antonio population denominators used for longer-term annual rates.

### Reference file

- `data/raw/ALL_Pedalcyclist_Fatal_Injury_Crashes.qry` — saved CRIS query used to create the export. It is retained for documentation but is not required to rerun the notebooks.

### Main output tables

- `outputs/san_antonio_annual.csv` — year-over-year San Antonio deaths and serious injuries.
- `outputs/commonalities.csv` — victim characteristics, road conditions and crash factors.
- `outputs/driver_factors_outcomes_2024_2026.csv` — contributing factors with deaths and serious injuries.
- `outputs/city_comparison.csv` — large-city comparison.
- `outputs/texas_cities_comparison_2024_2026.csv` — Texas places with at least 65,000 residents.
- `outputs/texas_cities_with_death_comparison_2024_2026.csv` — Texas places with at least one bicyclist death.
- `outputs/census_tract_hotspots.csv` — Census tract totals.
- `outputs/intersection_hotspots.csv` — intersection-area totals.
- `outputs/council_districts.csv` — City Council district totals.
- `outputs/official_bicycle_hin_2019_2023.csv` and `outputs/official_bicycle_hin_2024_2026.csv` — official HIN corridor comparisons.
- `outputs/candidate_corridors_2024_2026.csv` — current exploratory repeat-crash corridors, created by the corridor-map notebook.

### Datawrapper-ready tables

- `outputs/datawrapper_sa_annual_trend.csv` — San Antonio annual trend.
- `outputs/datawrapper_top10_city_rates.csv` — comparison chart data.
- `outputs/datawrapper_bike_commute_vs_death_rate.csv` — bike-commute share and death-rate comparison.

## Definitions

The CRIS export uses person-level filters:

- `Person Type = 3 - PEDALCYCLIST`
- `Person Injury Severity = K - FATAL INJURY` **OR** `A - SUSPECTED SERIOUS INJURY`

People are counted for injury and death totals. Crashes are deduplicated by `Crash ID` when the unit of analysis is a crash.

“Contributing factors” means factors recorded by police in CRIS. They do not independently establish legal fault or causation.

## Install

```bash
python -m pip install -r requirements.txt
```
