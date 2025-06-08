# Business Requirement Document: Automated ALM Reporting & Analytics

- **Project:** Automated ALM Reporting & NII Sensitivity Analysis
- **Client:** Indus National Bank (INB)
- **Version:** 1.0
- **Date:** June 8, 2025
- **Author:** Tharun Kumar Gajula, Business Analyst, EXL

---

## 1. Business Problem

Indus National Bank's (INB) Treasury and Risk departments currently face significant challenges with their Asset-Liability Management (ALM) processes. The existing workflow for analyzing **Interest Rate Risk in the Banking Book (IRRBB)** and Liquidity Risk is highly manual, relying on disparate spreadsheets.

This leads to several critical issues:
- **Delayed Reporting:** The generation of key reports for the **Asset Liability Committee (ALCO)** is slow, hindering timely and strategic decision-making.
- **Operational Risk:** Manual processes are prone to human error, raising concerns about data accuracy and regulatory compliance.
- **Inadequate Analysis:** The current setup does not allow for dynamic analysis, such as simulating the impact of potential **RBI** interest rate changes on the bank's **Net Interest Income (NII)** in a swift manner. This is a major concern for the **ALCO**, which needs to proactively manage the bank's profitability and risk exposure.

---

## 2. Project Goals & Objectives

The primary goal of this project is to develop a proof-of-concept (PoC) solution that demonstrates the value of automating INB's ALM reporting and analytics framework.

| Objective ID | Objective Description | Key Metric |
| :--- | :--- | :--- |
| **OBJ-01** | Automate the calculation of the bank's interest rate sensitivity gap. | Reduce time for Gap Analysis reporting from 2 days to under 1 hour. |
| **OBJ-02** | Enable dynamic **NII Sensitivity Analysis** against rate shocks. | Allow ALCO to view NII impact for a +/- 200 bps shock scenario on demand. |
| **OBJ-03** | Automate the calculation of the **Liquidity Coverage Ratio (LCR)**. | Ensure daily, accurate calculation of LCR to meet **RBI guidelines**. |
| **OBJ-04** | Establish a foundation for robust **Data Lineage** and quality. | Create a single, traceable workflow from raw data to final report, aligning with **BCBS 239** principles. |

---

## 3. Scope

### 3.1 In-Scope

- Development of a Python-based analytical engine to perform core ALM calculations.
- Analysis of **IRRBB** through **Gap Analysis** and **NII Sensitivity**.
- Analysis of Liquidity Risk through **LCR** calculation.
- Generation of automated reports for Gap, NII, and LCR.
- Use of simulated data representing the bank's core assets and liabilities.

### 3.2 Out-of-Scope

- Calculation of **Economic Value of Equity (EVE)** sensitivity.
- Implementation of the **Net Stable Funding Ratio (NSFR)**.
- Integration with the bank's live **Data Lake** or core banking system (the PoC will use CSV files).
- Development of a front-end user interface.

---

## 4. Key Stakeholders

| Stakeholder | Title | Role / Interest |
| :--- | :--- | :--- |
| **ALCO** | Asset Liability Committee | Primary consumer of the reports for strategic decisions. |
| **Head of Treasury** | Treasury Dept. | Management of daily liquidity, funding, and NII. |
| **Chief Risk Officer** | Risk Management | Oversight of **IRRBB** and Liquidity Risk compliance. |
| **Head of IT** | IT Department | Feasibility of integrating the final solution. |