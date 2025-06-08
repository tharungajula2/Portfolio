# Functional Requirement Document: ALM Analytical Engine

- **Project:** Automated ALM Reporting & NII Sensitivity Analysis
- **Client:** Indus National Bank (INB)
- **Version:** 1.0
- **Date:** June 7, 2025
- **Author:** [Your Name], Business Analyst, EXL

---

## 1. Introduction

This document provides the detailed functional requirements for the ALM Analytical Engine proof-of-concept. It expands on the business needs outlined in the `BRD_ALM_Reporting.md` (Version 1.0) and defines the specific logic, data processing steps, and outputs required.

## 2. Data Requirements

The engine will source data from two CSV files, simulating an extract from the bank's **Data Lake**.

| File | Field Name | Data Type | Description |
| :--- | :--- | :--- | :--- |
| **`assets.csv`** | `id` | String | Unique identifier for the asset |
| | `product_type`| String | e.g., 'Home Loan', 'Car Loan', 'G-Sec', 'Corp Bond' |
| | `amount` | Float | Outstanding principal amount in INR Crores |
| | `maturity_date`| Date (YYYY-MM-DD)| The final maturity date of the asset |
| | `interest_rate`| Float | The annual interest rate (e.g., 8.5 for 8.5%) |
| | `rate_type` | String | 'Fixed' or 'Floating' |
| | `repricing_period_days`| Integer | For 'Floating' assets, the repricing frequency in days (e.g., 365) |
| | `is_hqla` | String | 'Level 1', 'Level 2A', 'Level 2B', 'No' |
| **`liabilities.csv`**| `id` | String | Unique identifier for the liability |
| | `product_type`| String | e.g., 'Savings', 'Current', 'Retail FD', 'Corporate FD'|
| | `amount` | Float | Total deposit amount in INR Crores |
| | `maturity_date`| Date (YYYY-MM-DD)| The maturity date for fixed deposits |
| | `interest_rate`| Float | The annual interest rate paid |
| | `rate_type` | String | 'Fixed' or 'Floating' |
| | `repricing_period_days`| Integer | For 'Floating' liabilities, repricing frequency in days |

## 3. Functional Logic & Calculations

### 3.1 FR-01: Data Loading & Quality Check (Supports OBJ-04)
- The system must load `assets.csv` and `liabilities.csv` from the `/data/raw_data/` directory.
- It must perform a **Quality Check**:
  - Verify that there are no null values in `amount` or `interest_rate` columns.
  - Ensure `maturity_date` is a valid date format.
  - Log a confirmation message: "Data Quality Check Passed. Records loaded: X assets, Y liabilities."
- This process establishes **Data Lineage** from source file to processing.

### 3.2 FR-02: IRRBB - Gap Analysis (Supports OBJ-01)
- The system must categorize all rate-sensitive assets and liabilities into the following time buckets based on their next repricing date (for floating) or maturity date (for fixed).
  - **Time Buckets:** 1-28 days, 29-90 days, 91-180 days, 181-365 days, 1-3 years, 3-5 years, >5 years.
- The system must calculate:
  - Total Rate Sensitive Assets (RSA) in each bucket.
  - Total Rate Sensitive Liabilities (RSL) in each bucket.
  - The **Gap** for each bucket (Gap = RSA - RSL).
  - The Cumulative Gap.
- The output must be a CSV file as defined in the reporting section.

### 3.3 FR-03: IRRBB - NII Sensitivity Analysis (Supports OBJ-02)
- The system must first calculate the baseline annual **NII**.
  - `Annual Interest Income = SUM(asset.amount * asset.interest_rate / 100)`
  - `Annual Interest Expense = SUM(liability.amount * liability.interest_rate / 100)`
  - `Baseline NII = Annual Interest Income - Annual Interest Expense`
- The system must then simulate a **parallel interest rate shock of +100 basis points (+1.0%)**.
  - Apply the shock: For all 'Floating' rate assets and liabilities, the new rate becomes `interest_rate + 1.0`.
  - Recalculate the NII with the new rates (`Shocked NII`).
  - Calculate the impact: `NII Impact = Shocked NII - Baseline NII`.
  - The output must be a text file summarizing the results.

### 3.4 FR-04: LST - LCR Calculation (Supports OBJ-03)
- The system must calculate the stock of **High-Quality Liquid Assets (HQLA)**.
  - Identify all assets marked as `is_hqla` = 'Level 1', 'Level 2A', 'Level 2B'.
  - Apply RBI-specified haircuts (assumed for PoC):
    - Level 1: 0% haircut
    - Level 2A: 15% haircut
    - Level 2B: 50% haircut
  - `Total HQLA = SUM(HQLA amounts after haircut)`
- The system must calculate Total Net Cash Outflows over the next 30 days.
  - Apply RBI-specified run-off rates to liabilities (assumed for PoC):
    - 'Savings' & 'Current' (stable retail): 5% run-off rate.
    - 'Retail FD' maturing within 30 days: 10% run-off.
    - 'Corporate FD' maturing within 30 days: 40% run-off.
  - `Total Net Outflows = SUM(liability amounts * run-off rate)`
- The system must calculate the **LCR**: `LCR % = (Total HQLA / Total Net Outflows) * 100`.

## 4. Reporting Requirements

| Report ID | Description | Format | Filename |
| :--- | :--- | :--- | :--- |
| **RPT-01** | Gap Analysis Report | CSV | `gap_analysis_report.csv` |
| **RPT-02** | NII Sensitivity Summary | TXT | `nii_sensitivity_report.txt` |
| **RPT-03** | LCR Summary | TXT | `lcr_summary_report.txt` |

## 5. Non-Functional Requirements
- **NFR-01 (Performance):** The entire script (data load, processing, report generation) should execute in under 60 seconds on a standard machine.
- **NFR-02 (Data Integrity):** The logic must ensure that no records are dropped silently during processing, upholding the principles of **BCBS 239**.