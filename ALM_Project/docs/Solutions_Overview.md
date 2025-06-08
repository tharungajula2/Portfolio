# Project Solution Overview: ALM Reporting & Analytics PoC

- **Project:** Automated ALM Reporting & NII Sensitivity Analysis
- **Client:** Indus National Bank (INB)
- **Author:** [Your Name], Business Analyst, EXL

---

## 1. Executive Summary

This document provides an overview of the proof-of-concept (PoC) solution developed to address Indus National Bank's challenges in ALM reporting. By creating a Python-based analytical engine, we successfully automated the core calculations for Interest Rate Risk in the Banking Book (IRRBB) and Liquidity Coverage Ratio (LCR), demonstrating a significant improvement over the existing manual processes.

## 2. The Solution

A modular Python script (`alm_engine.py`) was developed to serve as the core of the solution. The engine performs the following key functions:

- **Data Loading & Validation:** Ingests raw data from CSV files and performs critical data quality checks, establishing a clear and auditable **Data Lineage** in line with **BCBS 239** principles.
- **Gap Analysis:** Automatically buckets rate-sensitive assets and liabilities into time horizons to generate a Gap Report, providing a clear view of the bank's asset-liability mismatch.
- **NII Sensitivity Analysis:** Calculates the bank's baseline Net Interest Income and simulates the impact of a +100 basis point interest rate shock on profitability.
- **LCR Calculation:** Computes the Basel III Liquidity Coverage Ratio by identifying High-Quality Liquid Assets (HQLA) and simulating a 30-day stress scenario of cash outflows.

## 3. Key Findings & Business Insights

The analysis performed by the engine yielded the following critical insights for the ALCO:

| Finding ID | Insight | Supporting Report | Business Implication |
| :--- | :--- | :--- | :--- |
| **FIN-01** | **The bank is liability-sensitive in the short term.** | `gap_analysis_report.csv` | There is a significant negative gap in the <1 year buckets, exposing the bank to rising interest rates. |
| **FIN-02** | **A +100 bps rate hike will reduce NII by ~₹3.58 Crores.** | `nii_sensitivity_report.txt` | This quantifies the bank's interest rate risk, showing a direct impact on profitability that needs to be managed or hedged. |
| **FIN-03** | **The bank's liquidity position is extremely strong.** | `lcr_summary_report.txt` | With a calculated **LCR of ~725%**, the bank is well above the 100% regulatory minimum and can comfortably withstand a liquidity crisis. |

## 4. Conclusion & Next Steps

This PoC successfully demonstrates that an automated, script-based approach can provide faster, more accurate, and deeper ALM insights for Indus National Bank. The next steps would be to expand the engine's capabilities to include EVE analysis and NSFR, and to integrate it with the bank's live data warehouse.

"As a next step, the alm_engine.py could be refactored into a modular package (/analytics) to improve scalability and maintainability, separating IRRBB, LST, and data loading logic into their own respective modules."