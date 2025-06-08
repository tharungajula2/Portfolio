
# ALM & Treasury Analytics Engine for Indian Banking

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)
[![Pandas](https://img.shields.io/badge/pandas-2.2-blue)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/numpy-1.26-blue)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is a comprehensive simulation of a Business Analyst's role in developing an Asset-Liability Management (ALM) and Treasury analytics solution for a mid-sized Indian bank. The engine analyzes Interest Rate Risk in the Banking Book (IRRBB) and Liquidity Risk, producing key regulatory and management reports.

---

## Table of Contents
- [Problem Statement](#problem-statement)
- [Solution Overview](#solution-overview)
- [Key Features](#key-features)
- [Key Business Insights](#key-business-insights)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Future Improvements](#future-improvements)

---

## Problem Statement

A simulated mid-sized Indian commercial bank, "Indus National Bank," was struggling with its manual, spreadsheet-based ALM reporting. The process was slow, error-prone, and could not provide the **Asset-Liability Committee (ALCO)** with timely insights into the bank's risk profile, especially concerning **Net Interest Income (NII)** sensitivity to **RBI** rate changes. This project was initiated to build a proof-of-concept automated solution.

## Solution Overview

A Python-based analytical engine was developed to automate the generation of critical ALM reports. The solution follows the principles of **BCBS 239** by ensuring clear **Data Lineage**, implementing data quality checks, and providing adaptable, on-demand risk analytics.

## Key Features

- **Data Validation**: A robust pre-check ensures the integrity of source data.
- **IRRBB Gap Analysis**: Generates a traditional Gap Report, bucketing rate-sensitive assets and liabilities to identify mismatches across time horizons.
- **NII Sensitivity Analysis**: Quantifies the impact on Net Interest Income (NII) under a +100 basis point parallel interest rate shock scenario.
- **LST LCR Calculation**: Calculates the Basel III Liquidity Coverage Ratio (LCR) by identifying High-Quality Liquid Assets (HQLA) and simulating stressed cash outflows over a 30-day period.

## Key Business Insights

The engine processed the bank's simulated balance sheet and produced the following actionable insights:

#### 1. The bank is Liability-Sensitive to Interest Rate Risk.
The Gap Report clearly shows a negative gap in the short-term buckets, exposing the bank to rising interest rates.

*(Your `gap_analysis_report.csv` screenshot would go here)*

#### 2. A +100 bps Rate Hike would decrease NII by ₹3.58 Crores.
The NII Sensitivity report confirms the Gap Analysis, quantifying the precise profit-at-risk.

*(Your `nii_sensitivity_report.txt` screenshot would go here)*

#### 3. The bank has a very Strong Liquidity Position.
The LCR is calculated at ~725%, well above the RBI's 100% minimum requirement.

*(Your `lcr_summary_report.txt` screenshot would go here)*

## Technology Stack

- **Language:** Python 3.11
- **Libraries:** Pandas, NumPy

## Project Structure
```
/ALM_Project
|-- /data
|   |-- /raw_data
|   |   |-- assets.csv
|   |   |-- liabilities.csv
|   |-- /processed_data
|-- /docs
|   |-- BRD_ALM_Reporting.md
|   |-- FRD_ALM_Engine.md
|   |-- Solution_Overview.md
|-- /reports
|   |-- gap_analysis_report.csv
|   |-- lcr_summary_report.txt
|   |-- nii_sensitivity_report.txt
|-- /src
|   |-- alm_engine.py
|   |-- data_generator.py
|-- .gitignore
|-- README.md
|-- TASKS.md
```

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone [your-github-repo-link]
   cd ALM_Project
   ```
2. **Create and activate the Conda environment:**
   ```bash
   conda create -n alm_project python=3.11 pandas numpy
   conda activate alm_project
   ```
3. **Run the analytical engine:**
   ```bash
   python src/alm_engine.py
   ```
   The reports will be generated in the `/reports` directory.

## Future Improvements

- **Modularization**: Refactor the `alm_engine.py` script into a modular package (`/analytics`) to improve scalability and maintainability, separating IRRBB and LST logic.
- **Expanded Scenarios**: Add more complex stress tests, such as non-parallel rate shocks (yield curve twists) and EVE (Economic Value of Equity) calculations.
- **Visualization**: Integrate libraries like Matplotlib or Seaborn to create visual dashboards for the reports.

