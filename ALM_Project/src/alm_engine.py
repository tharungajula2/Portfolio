import pandas as pd
import os
from datetime import datetime

# --- Configuration ---
REPORTS_DIR = 'reports'
DATA_DIR = 'data/raw_data'
ASSET_FILE = os.path.join(DATA_DIR, 'assets.csv')
LIABILITY_FILE = os.path.join(DATA_DIR, 'liabilities.csv')
BASE_DATE = datetime.strptime('2025-06-07', '%Y-%m-%d') # Our project's 'today'

def load_and_validate_data():
    """
    Loads asset and liability data from CSV files and performs quality checks.
    This function directly implements FR-01 and aligns with BCBS 239.
    """
    print("--- Starting ALM Engine ---")
    print("Step 1: Loading and Validating Data...")

    # Load data from the 'raw_data' directory, establishing Data Lineage
    assets_df = pd.read_csv(ASSET_FILE)
    liabilities_df = pd.read_csv(LIABILITY_FILE)

    # --- Data Quality Checks (BCBS 239 - Accuracy & Integrity) ---

    # 1. Check for null values in critical columns
    critical_asset_cols = ['amount', 'interest_rate']
    critical_liability_cols = ['amount', 'interest_rate']
    
    if assets_df[critical_asset_cols].isnull().any().any():
        raise ValueError("Error: Missing critical data in assets file.")
    
    if liabilities_df[critical_liability_cols].isnull().any().any():
        raise ValueError("Error: Missing critical data in liabilities file.")

    # 2. Convert date columns to proper datetime objects
    assets_df['maturity_date'] = pd.to_datetime(assets_df['maturity_date'])
    # For liabilities, handle the 'None' values for non-maturity products
    liabilities_df['maturity_date'] = pd.to_datetime(liabilities_df['maturity_date'], errors='coerce')

    print(f"Data Quality Check Passed. Records loaded: {len(assets_df)} assets, {len(liabilities_df)} liabilities.")
    
    return assets_df, liabilities_df


def perform_gap_analysis(assets_df, liabilities_df):
    """
    Performs IRRBB Gap Analysis based on FR-02.
    Calculates the mismatch between rate-sensitive assets and liabilities.
    """
    print("Step 2: Performing Gap Analysis...")
    os.makedirs(REPORTS_DIR, exist_ok=True)

    # Determine the days to repricing for each instrument
    assets_df['days_to_repricing'] = (assets_df['maturity_date'] - BASE_DATE).dt.days
    assets_df.loc[assets_df['rate_type'] == 'Floating', 'days_to_repricing'] = assets_df['repricing_period_days']

    liabilities_df['days_to_repricing'] = (liabilities_df['maturity_date'] - BASE_DATE).dt.days
    liabilities_df.loc[liabilities_df['rate_type'] == 'Floating', 'days_to_repricing'] = liabilities_df['repricing_period_days']
    
    # Define the time buckets as per the FRD
    bins = [0, 28, 90, 180, 365, 365*3, 365*5, float('inf')]
    labels = ['1-28 days', '29-90 days', '91-180 days', '181-365 days', '1-3 years', '3-5 years', '>5 years']

    # Assign each asset and liability to a time bucket
    assets_df['bucket'] = pd.cut(assets_df['days_to_repricing'], bins=bins, labels=labels, right=False)
    liabilities_df['bucket'] = pd.cut(liabilities_df['days_to_repricing'], bins=bins, labels=labels, right=False)

    # --- THIS IS THE CORRECTED LOGIC ---
    # Aggregate amounts in each bucket. `observed=True` silences the FutureWarning.
    asset_gap = assets_df.groupby('bucket', observed=True)['amount'].sum().reset_index().rename(columns={'amount': 'Assets'})
    liability_gap = liabilities_df.groupby('bucket', observed=True)['amount'].sum().reset_index().rename(columns={'amount': 'Liabilities'})

    # Create the gap report
    gap_report = pd.merge(asset_gap, liability_gap, on='bucket', how='outer')
    # Specifically fill NA on the numeric columns only
    gap_report[['Assets', 'Liabilities']] = gap_report[['Assets', 'Liabilities']].fillna(0)
    
    gap_report['Gap (Assets - Liabilities)'] = gap_report['Assets'] - gap_report['Liabilities']
    gap_report['Cumulative Gap'] = gap_report['Gap (Assets - Liabilities)'].cumsum()

    # Save the report to a CSV file
    report_path = os.path.join(REPORTS_DIR, 'gap_analysis_report.csv')
    gap_report.to_csv(report_path, index=False)
    
    print(f"Gap Analysis complete. Report saved to '{report_path}'")
    return gap_report


def calculate_nii_sensitivity(assets_df, liabilities_df):
    """
    Calculates NII and its sensitivity to a rate shock, based on FR-03.
    """
    print("Step 3: Calculating NII Sensitivity...")

    # --- Baseline NII Calculation ---
    assets_df['interest_income'] = assets_df['amount'] * assets_df['interest_rate'] / 100
    liabilities_df['interest_expense'] = liabilities_df['amount'] * liabilities_df['interest_rate'] / 100

    total_income = assets_df['interest_income'].sum()
    total_expense = liabilities_df['interest_expense'].sum()
    baseline_nii = total_income - total_expense

    # --- Shock Scenario (+100 bps) ---
    rate_shock = 1.0  # +100 basis points

    # Apply shock only to 'Floating' rate instruments
    assets_shocked = assets_df.copy()
    liabilities_shocked = liabilities_df.copy()

    assets_shocked.loc[assets_shocked['rate_type'] == 'Floating', 'interest_rate'] += rate_shock
    liabilities_shocked.loc[liabilities_shocked['rate_type'] == 'Floating', 'interest_rate'] += rate_shock

    # Recalculate income and expense after shock
    assets_shocked['interest_income'] = assets_shocked['amount'] * assets_shocked['interest_rate'] / 100
    liabilities_shocked['interest_expense'] = liabilities_shocked['amount'] * liabilities_shocked['interest_rate'] / 100

    shocked_income = assets_shocked['interest_income'].sum()
    shocked_expense = liabilities_shocked['interest_expense'].sum()
    shocked_nii = shocked_income - shocked_expense

    # --- Generate Report ---
    nii_impact = shocked_nii - baseline_nii

    report_content = f"""
=================================================
=      Net Interest Income (NII) Sensitivity Report     =
=================================================
All amounts in INR Crores.

Scenario: +100 Basis Point (+{rate_shock}%) Parallel Rate Shock

--- BASELINE ---
Total Interest Income:  {total_income:,.2f}
Total Interest Expense: {total_expense:,.2f}
---------------------------------
Baseline NII:           {baseline_nii:,.2f}

--- AFTER SHOCK ---
Shocked Interest Income:  {shocked_income:,.2f}
Shocked Interest Expense: {shocked_expense:,.2f}
---------------------------------
Shocked NII:              {shocked_nii:,.2f}

=================================================
=                      IMPACT                     =
=================================================
Change in NII:          {nii_impact:,.2f}
=================================================
"""

    report_path = os.path.join(REPORTS_DIR, 'nii_sensitivity_report.txt')
    with open(report_path, 'w') as f:
        f.write(report_content)

    print(f"NII Sensitivity analysis complete. Report saved to '{report_path}'")


def calculate_lcr(assets_df, liabilities_df):
    """
    Calculates the Liquidity Coverage Ratio (LCR) based on FR-04.
    """
    print("Step 4: Calculating Liquidity Coverage Ratio (LCR)...")

    # --- Calculate Stock of High-Quality Liquid Assets (HQLA) ---
    haircuts = {'Level 1': 0, 'Level 2A': 0.15, 'Level 2B': 0.50} # 15% and 50% haircuts

    hqla_assets = assets_df[assets_df['is_hqla'] != 'No'].copy()
    hqla_assets['haircut_pct'] = hqla_assets['is_hqla'].map(haircuts)
    hqla_assets['post_haircut_value'] = hqla_assets['amount'] * (1 - hqla_assets['haircut_pct'])

    total_hqla = hqla_assets['post_haircut_value'].sum()

    # --- Calculate Net Cash Outflows over 30 days ---
    run_off_rates = {
        'Savings': 0.05,       # Stable retail deposits
        'Current': 0.05,       # Stable retail deposits
        'Retail FD': 0.10,     # Less stable retail
        'Corporate FD': 0.40  # Unsecured wholesale funding
    }

    # Non-maturity deposits (Savings, Current) are subject to run-off
    non_maturity_liab = liabilities_df[liabilities_df['product_type'].isin(['Savings', 'Current'])].copy()
    non_maturity_liab['run_off_rate'] = non_maturity_liab['product_type'].map(run_off_rates)
    non_maturity_outflow = (non_maturity_liab['amount'] * non_maturity_liab['run_off_rate']).sum()

    # Maturity deposits (FDs) only run-off if they mature within the next 30 days
    days_to_maturity_30 = (liabilities_df['maturity_date'] - BASE_DATE).dt.days <= 30
    maturity_liab = liabilities_df[days_to_maturity_30].copy()
    maturity_liab['run_off_rate'] = maturity_liab['product_type'].map(run_off_rates)
    maturity_outflow = (maturity_liab['amount'] * maturity_liab['run_off_rate']).sum()

    total_outflows = non_maturity_outflow + maturity_outflow

    # --- Calculate Final LCR ---
    lcr = (total_hqla / total_outflows) * 100 if total_outflows > 0 else float('inf')

    # --- Generate Report ---
    report_content = f"""
=================================================
=         Liquidity Coverage Ratio (LCR) Report         =
=================================================
As per Basel III / RBI Guidelines (Simulated)
All amounts in INR Crores.

--- A. STOCK OF HIGH-QUALITY LIQUID ASSETS (HQLA) ---
Total HQLA (Post-Haircut):   {total_hqla:,.2f}

--- B. TOTAL NET CASH OUTFLOWS (Next 30 Days) ---
Total Outflows:              {total_outflows:,.2f}

=================================================
=                       LCR                       =
=================================================
LCR Percentage (A / B):     {lcr:.2f}%
RBI Minimum Requirement:    100.00%
=================================================
"""
    report_path = os.path.join(REPORTS_DIR, 'lcr_summary_report.txt')
    with open(report_path, 'w') as f:
        f.write(report_content)

    print(f"LCR analysis complete. Report saved to '{report_path}'")



def main():
    """
    Main function to run the ALM analysis.
    """
    assets, liabilities = load_and_validate_data()

    gap_report = perform_gap_analysis(assets, liabilities)
    gap_report = gap_report.round(2)
    gap_report.to_csv(os.path.join(REPORTS_DIR, 'gap_analysis_report.csv'), index=False)

    calculate_nii_sensitivity(assets, liabilities)

    # Add the final LCR analysis step
    calculate_lcr(assets, liabilities)

    print("\n--- ALM Engine Run Finished ---")

 

# --- Main Execution ---
if __name__ == "__main__":
    main()