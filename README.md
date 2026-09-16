# San Antonio bicyclist crash analysis

Reproducible analysis of Texas CRIS records for pedalcyclists killed or suspected seriously injured in crashes from 2016 through Sept. 1, 2026.

The current reporting window is **2024 through Sept. 1, 2026**. Treat it as one reporting period; 2026 is included through the latest available CRIS date.

## Run these notebooks

### 1. Main analysis

`san_antonio_bicyclist_crashes.ipynb`

Run this first. It creates the main story tables:

- annual San Antonio deaths and serious injuries;
- Texas city comparison rates;
- bicycle commute comparisons;
- Census tract hotspots;
- City Council district totals;
- crash commonalities, including helmet status and contributing factors; and
- official HIN comparison tables.

### 2. Current corridor map

`candidate_corridors_victim_map_no_hin.ipynb`

Run this after the main notebook. It uses the local CRIS and Streets files to identify repeat-crash roadway stretches from 2024 through Sept. 1, 2026.

It does **not** call the official HIN API. It creates:

- `outputs/candidate_corridors_2024_2026.csv`
- `outputs/candidate_corridors_victim_map_2024_2026.html`

The HTML map includes street context, highlighted candidate corridors, clickable crash points, deaths versus serious injuries, victim age/gender, helmet status, contributing factors and coordinates. These are exploratory candidate corridors, not an official City ranking.

### 3. Historical City HIN comparison

`recreate_bicycle_hin_method.ipynb`

Use this only to compare the City's earlier High Injury Network analysis with the current period. It is separate from the current corridor map.

### 4. Datawrapper charts

`publish_datawrapper_charts.ipynb`

Run after the main notebook. It creates and publishes the three chart datasets/charts using a Datawrapper API token entered locally. The token is not stored in the notebook.

## Data files

### Raw inputs

- `data/raw/myexport_final.csv` — TxDOT CRIS export.
- `data/raw/ALL_Pedalcyclist_Fatal_Injury_Crashes.qry` — saved CRIS query.
- `data/raw/Streets.zip` — San Antonio street centerline layer used by the corridor map.
- `data/population_estimates.csv` — population denominators used by the analysis.

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

### Datawrapper-ready tables

- `outputs/datawrapper_sa_annual_trend.csv` — San Antonio annual trend.
- `outputs/datawrapper_top10_city_rates.csv` — comparison chart data.
- `outputs/datawrapper_bike_commute_vs_death_rate.csv` — commute share and death-rate comparison.

## Definitions

The CRIS export uses person-level filters:

- `Person Type = 3 - PEDALCYCLIST`
- `Person Injury Severity = K - FATAL INJURY` **OR** `A - SUSPECTED SERIOUS INJURY`

People are counted for injury and death totals. Crashes are deduplicated by `Crash ID` when the unit of analysis is a crash. “Contributing factors” means factors recorded by police in CRIS; it does not independently establish legal fault or causation.

## Install

```bash
python -m pip install -r requirements.txt
```
