# San Antonio bicyclist crash analysis

Reproducible analysis of Texas CRIS records for pedalcyclists killed or suspected seriously injured in crashes from 2016 through Sept. 1, 2026.

## Main notebook

Open `san_antonio_bicyclist_crashes.ipynb` in Jupyter or VS Code and run all cells. It produces editor-ready CSV tables and PNG charts in `outputs/`.

## HIN-method recreation

Open `recreate_bicycle_hin_method.ipynb` to independently rank roadway segments using the City's publicly described High Injury Network approach and identify candidate new trouble spots in the 2024–Sept. 1, 2026 reporting window. This is an independent recreation, not the City's official calculation.

The notebook covers:

- San Antonio year-over-year serious injuries and deaths;
- comparison with Houston, Austin, Dallas, Fort Worth and El Paso;
- comparison with all Texas places of at least 65,000 residents, using raw counts and rates per 1 million residents; the displayed ranking is limited to places with at least one bicyclist death;
- population-adjusted rates for the 2024–Sept. 1, 2026 reporting window, using the average 2024–2025 population because no 2026 estimate is available;
- Census tract hotspots;
- San Antonio City Council districts; and
- the City of San Antonio's official bicycle High Injury Network corridors, with separate death and suspected-serious-injury counts for 2019–2023 and 2021–2026;
- common features of the severe-injury and fatal crashes, including intersection context, helmet status and contributing-factor codes; and
- a 2024–Sept. 1, 2026 reporting-window update, matching the latest CRIS records.

## Definitions

The CRIS export was built with person-level filters:

- `Person Type = 3 - PEDALCYCLIST`
- `Person Injury Severity = K - FATAL INJURY` **OR** `A - SUSPECTED SERIOUS INJURY`

People are counted for injury and death totals. Crashes are deduplicated by `Crash ID` when the unit of analysis is a crash.

The current reporting window runs through Sept. 1, 2026, matching the latest date in the CRIS export.

## Sources

- TxDOT CRIS export: `data/raw/myexport_final.csv`.
- Saved CRIS query: `data/raw/ALL_Pedalcyclist_Fatal_Injury_Crashes.qry`
- Census population estimates: `data/population_estimates.csv`
- 2024 American Community Survey 1-year population API: used for the Texas places comparison (places with populations of at least 65,000)
- Census TIGER/Line 2020 tract boundaries: downloaded by the notebook
- City of San Antonio council districts: downloaded by the notebook from the official Open Data SA ArcGIS service
- City of San Antonio Bicycle High Injury Network corridors: downloaded by the notebook from the official ArcGIS service

The population file combines the Census Bureau's 2010–2020 intercensal estimates for 2016–2019 with its 2020–2025 estimates for 2020–2025. For the current comparison, the notebook uses the average 2024–2025 population as the denominator because a 2026 estimate is not available. It is a resident-population comparison, not a measure of individual cyclist risk or miles traveled.

## Install

```bash
python -m pip install -r requirements.txt
```
