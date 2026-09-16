# San Antonio bicyclist crash analysis

Reproducible analysis of Texas CRIS records for pedalcyclists killed or suspected seriously injured in crashes from 2016 through Sept. 1, 2026.

## Main notebook

Open `san_antonio_bicyclist_crashes.ipynb` in Jupyter or VS Code and run all cells. It produces editor-ready CSV tables and PNG charts in `outputs/`.

It covers:

- San Antonio year-over-year serious injuries and deaths;
- Texas city comparisons for the 2024–Sept. 1, 2026 reporting window;
- rates per 1 million residents and bike-commute shares;
- Census tract hotspots and City Council districts;
- victim characteristics, helmet status and police-recorded contributing factors; and
- official City bicycle High Injury Network comparisons.

## Current corridor map

Open `candidate_corridors_victim_map_no_hin.ipynb` to create the current-period corridor analysis and clickable map.

This notebook uses all qualifying San Antonio crashes from 2024 through Sept. 1, 2026 and the local Streets layer. It does not call the official HIN API. It identifies repeat-crash roadway stretches using a transparent bounded grouping rule and displays each crash as a clickable point with:

- deaths and serious injuries;
- victim age and gender;
- helmet status;
- police-recorded contributing factors; and
- road name and coordinates.

These are exploratory candidate corridors, not an official City ranking.

## HIN-method recreation

Open `recreate_bicycle_hin_method.ipynb` only when comparing the City's earlier High Injury Network work with the current period. It is a separate historical comparison and does not drive the current corridor map.

## Publish charts to Datawrapper

Run `publish_datawrapper_charts.ipynb` after running the main analysis notebook. It prompts for a Datawrapper API token, finds the San Antonio folder (or lets you enter its folder ID), creates three charts, publishes them and prints their URLs. The token is not stored in the notebook.

## Definitions

The CRIS export was built with person-level filters:

- `Person Type = 3 - PEDALCYCLIST`
- `Person Injury Severity = K - FATAL INJURY` **OR** `A - SUSPECTED SERIOUS INJURY`

People are counted for injury and death totals. Crashes are deduplicated by `Crash ID` when the unit of analysis is a crash.

The current reporting window runs through Sept. 1, 2026, matching the latest date in the CRIS export.

## Sources

- TxDOT CRIS export: `data/raw/myexport_final.csv`
- Saved CRIS query: `data/raw/ALL_Pedalcyclist_Fatal_Injury_Crashes.qry`
- San Antonio Streets layer: `data/raw/Streets.zip`
- Census population estimates: `data/population_estimates.csv`
- 2024 American Community Survey 1-year population API: used for the Texas places comparison
- 2024 American Community Survey table B08301: bicycle commuters (`B08301_018E`) divided by workers (`B08301_001E`)
- Census TIGER/Line 2020 tract boundaries: downloaded by the notebook
- City of San Antonio council districts: downloaded by the notebook from the official Open Data SA ArcGIS service
- City of San Antonio Bicycle High Injury Network corridors: used only for the official-HIN comparison notebook

The population file combines the Census Bureau's 2010–2020 intercensal estimates for 2016–2019 with its 2020–2025 estimates for 2020–2025. For the current comparison, the notebook uses the average 2024–2025 population as the denominator because a 2026 estimate is not available. It is a resident-population comparison, not a measure of individual cyclist risk or miles traveled.

## Install

```bash
python -m pip install -r requirements.txt
```
