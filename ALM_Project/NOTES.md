Objective is to create a complete, end-to-end simulation that transforms you from a candidate into a practitioner. I'll play the role of Business Analyst tasked with solving a critical ALM problem for a pseudo client bank. I will build everything as shown below and showcase it on GitHub.

Here is the project blueprint.

***

## Project: ALM Reporting & NII Sensitivity Analysis for Indus National Bank

### **Project Synopsis**

* **Client:** Indus National Bank (INB), a mid-sized Indian commercial bank.
* **Problem Statement:** INB's Treasury and Risk teams are struggling with their ALM reporting. The process for calculating **Interest Rate Risk in the Banking Book (IRRBB)** and the **Liquidity Coverage Ratio (LCR)** is manual, slow, and heavily reliant on spreadsheets. Following a recent **RBI repo rate** hike, their ALCO is demanding faster, more accurate insights into their **Net Interest Income (NII)** sensitivity. They are also concerned about their compliance with **BCBS 239** principles regarding data lineage and quality.
* **Your Role:** You are the Lead Business Analyst from EXL, brought in to develop a proof-of-concept (PoC) solution. Your job is to understand their requirements, analyze their data, build a prototype analytical engine in Python, and present a solution.
* **Project Goal:** Deliver a Python-based prototype that automates key ALM calculations and demonstrates the value of EXL's analytical services. This project will serve as your capstone, showcasing your domain knowledge and technical BA skills.

### **Simulated Tools & Workflow**

Since I don't have Jira, Confluence, or SharePoint, I'll use a professional local file structure that mimics them. This is a common practice.

* **Confluence (Wiki/Documentation):** Your main `README.md` file and other documents in a `/docs` folder.
* **Jira (Task Management):** We'll create a simple `TASKS.md` file to list and track our project tasks, simulating a sprint backlog.
* **SharePoint (Document Repository):** Your `/docs` folder will serve as the central repository for your BRD, FRD, and final presentation.

---

## The One-Day Project Plan: A Step-by-Step Simulation

### **Phase 0: Project Setup & Environment (Approx: 30 minutes)**

This is your project's foundation.

1.  **Create my Project Directory:** On my computer, create a main folder. Let's call it `ALM_Project`.
2.  **Set Up the Folder Structure:** Inside `ALM_Project`, create the following structure. This keeps your work organized and professional for GitHub.
    ```
    /ALM_Project
    |-- /data
    |   |-- /raw_data
    |   |-- /processed_data
    |-- /docs
    |-- /reports
    |-- /src
    |-- README.md
    |-- TASKS.md
    |-- .gitignore 
    ```
3.  **Set Up my Python Environment:** In VS Code, open the `ALM_Project` folder. Create a virtual environment and install the necessary libraries:
    ```bash
    conda create -n alm_project python=3.12
    conda activate alm_project
    conda install pandas numpy
    ```
4.  **Define my Tasks:** Open `TASKS.md` and list the high-level tasks from the phases below. This simulates your role in sprint planning with a **Scrum Master**.

---

### **Phase 1: Discovery & Requirements (Approx: 2 hours)**

Here, you put on your pure Business Analyst hat. You will create the key documents that drive the entire project.

1.  **Business Requirement Document (BRD):**
    * **Tool:** Create a new file: `docs/BRD_ALM_Reporting.md`.
    * **Content:** Write a high-level BRD. It should define the business problem, project objectives, scope, and key stakeholders (ALCO, Head of Treasury, Chief Risk Officer at INB).
    * **Keywords to include:** *Asset-Liability Mismatch, IRRBB, LST, NII, NIM, EVE, ALCO, RBI Guidelines, Regulatory Reporting.*
    * **Focus:** Write from a business perspective. *Why* does the bank need this? What are the goals? (e.g., "Reduce reporting turnaround time by 50%", "Enable dynamic NII sensitivity analysis for different rate shock scenarios").

2.  **Functional Requirement Document (FRD):**
    * **Tool:** Create a new file: `docs/FRD_ALM_Engine.md`.
    * **Content:** Get more specific. Translate the BRD into functional requirements for the Python engine you're about to build.
    * **Keywords to include:** *Data Lineage, Data Lake (as a source), Quality Check, Gap Analysis, NII Sensitivity Calculation (+/- 200 bps shock), HQLA Classification (Level 1, Level 2), LCR Calculation, SQL (as a concept for data extraction).*
    * **Structure:** Use sections like:
        * **Data Requirements:** Detail the exact data fields needed from the bank's "Data Lake" (e.g., for loans: account_id, amount, maturity_date, interest_rate, rate_type F/V, repricing_benchmark).
        * **Functional Logic:** Specify the calculation rules. (e.g., "The system must calculate the repricing gap for time buckets: 1-28 days, 29-90 days...", "The system must apply a +100bps parallel shift to all floating rate instruments to calculate the impact on NII.").
        * **Reporting Requirements:** Define the output format. (e.g., "The LCR report must be a CSV file named `LCR_Report_YYYYMMDD.csv`").

---

### **Phase 2: Data Simulation & Python Development (Approx: 4 hours)**

This is the core technical phase where I build the solution.

1.  **Data Generation (Simulating the Data Lake):**
    * **Tool:** Create a Python script: `src/data_generator.py`.
    * **Action:** Write a Python function that uses Pandas and NumPy to create a pseudo balance sheet for Indus National Bank.
    * **Create two CSV files** and save them in the `/data/raw_data/` folder:
        * `assets.csv`: Include columns for loans and investments. Add attributes like `id`, `product_type` (Car Loan, Home Loan, G-Sec), `amount`, `maturity_date`, `interest_rate`, `rate_type` ('Fixed', 'Floating'). Make sure to include **G-Secs** and highly-rated corporate bonds to act as **HQLA**.
        * `liabilities.csv`: Include columns for deposits. Add `id`, `product_type` (Savings, Current, Fixed Deposit), `amount`, `maturity_date`.

2.  **The ALM Engine (Your Solution):**
    * **Tool:** Create main script: `src/alm_engine.py`.
    * **Action:** This is where I implement your FRD. Structure my script with clear functions.

    * **Step 2a: Data Loading & Quality Check (BCBS 239):**
        * Load `assets.csv` and `liabilities.csv` into Pandas DataFrames.
        * Perform quality checks: check for null values, ensure data types are correct. Print a "Data Quality Check Passed" message. This demonstrates your understanding of **Data Lineage** and quality.

    * **Step 2b: IRRBB - Gap Analysis & NII Sensitivity:**
        * Write a function to perform **Gap Analysis**. Create time buckets (e.g., 0-30d, 31-90d, 91-180d, etc.). Categorize all assets and liabilities into these buckets based on their repricing or maturity dates. The result is a gap report showing the net mismatch in each bucket.
        * Write a function to calculate the baseline **NII**. (Total Interest from Assets - Total Interest from Liabilities).
        * Write a function to simulate an interest rate shock (e.g., `rate_shock = +1.00`%). Apply this shock to all 'Floating' rate items. Recalculate the NII and show the impact. This is the **NII Sensitivity Analysis**.

    * **Step 2c: LST - LCR Calculation:**
        * Write a function to identify **HQLA**. From the `assets.csv`, filter for assets that qualify as HQLA (e.g., 'G-Secs' are Level 1, top-rated 'Corporate Bonds' could be Level 2a with a haircut). Calculate the total stock of HQLA.
        * Write a function to simulate **Net Cash Outflows** over 30 days. Apply RBI-prescribed runoff rates (you can assume these, e.g., 5% for retail deposits, 30% for corporate deposits).
        * Calculate the **LCR**: `LCR = Stock of HQLA / Total Net Cash Outflows over 30 days`.

3.  **Generate Reports:**
    * Your `alm_engine.py` script should save its output to the `/reports` folder.
    * **Outputs:**
        * `gap_analysis_report.csv`
        * `nii_sensitivity_report.txt` (a simple text file summarizing the NII impact)
        * `lcr_summary_report.txt` (showing HQLA, Net Outflows, and the final LCR percentage)

---

### **Phase 3: Delivery & Showcase (Approx: 1.5 hours)**

You've built the solution. Now, you need to present it and prepare it for GitHub.

1.  **Create a Solution Document:**
    * **Tool:** Create a new file: `docs/Solution_Overview.md`.
    * **Action:** Write a brief summary explaining the solution you built. Describe the Python engine, the key features (IRRBB, LCR), and the results you found (e.g., "The analysis shows that in a +100bps shock scenario, INB's NII is projected to decrease by 5.7%, indicating a liability-sensitive balance sheet."). This shows you can **interpret ALM data in functional terms**.

2.  **Prepare your GitHub README:**
    * **Tool:** Edit the main `README.md`. This is the most important file in your repository.
    * **Action:** Structure it like a professional project page. Include sections for:
        * Project Title
        * Problem Statement (copied from your BRD)
        * Solution Overview (summarizing your `Solution_Overview.md`)
        * Technology Stack (Python, Pandas, NumPy)
        * How to Run the Project (instructions on setting up the environment and running `alm_engine.py`)
        * Project Structure (explain your folder layout)
        * Key Findings (a bulleted list of your ALM analysis results)

3.  **Final Push to GitHub:**
    * Create a new repository on GitHub.
    * Initialize a git repository in your local folder, commit all your files, and push them to GitHub.

By the end of the Project, I will have a complete, professional-looking GitHub repository that demonstrates a full project cycle. Working through the BRD, the FRD, the Python code, the challenges (**Data Quality**), and the solution delivered, hitting every thing I need to learn.