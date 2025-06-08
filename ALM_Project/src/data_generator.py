import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# --- Configuration ---
NUM_ASSETS = 500
NUM_LIABILITIES = 1000
DATA_DIR = 'data/raw_data'
ASSET_FILE = os.path.join(DATA_DIR, 'assets.csv')
LIABILITY_FILE = os.path.join(DATA_DIR, 'liabilities.csv')
BASE_DATE = datetime.strptime('2025-06-07', '%Y-%m-%d') # Our project's 'today'
np.random.seed(42) # for reproducibility

# --- Helper Functions ---
def create_directories():
    """Creates the necessary directories if they don't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)

def generate_assets():
    """Generates a DataFrame of pseudo bank assets."""
    asset_types = ['Home Loan', 'Car Loan', 'Personal Loan', 'G-Sec', 'Corp Bond']
    rate_types = ['Fixed', 'Floating']
    hqla_levels = ['Level 1', 'Level 2A', 'No'] # Simplified for PoC

    data = {
        'id': [f'ASSET_{i+1:04d}' for i in range(NUM_ASSETS)],
        'product_type': np.random.choice(asset_types, NUM_ASSETS, p=[0.3, 0.2, 0.2, 0.2, 0.1]),
        'amount': np.round(np.random.uniform(0.05, 5, NUM_ASSETS), 2), # in INR Crores
        'interest_rate': np.round(np.random.uniform(7.5, 14.0, NUM_ASSETS), 2),
        'rate_type': np.random.choice(rate_types, NUM_ASSETS, p=[0.6, 0.4]),
        'repricing_period_days': np.random.choice([180, 365, 1095], NUM_ASSETS)
    }

    # Generate maturity dates
    maturities = [BASE_DATE + timedelta(days=int(d)) for d in np.random.uniform(365, 365*10, NUM_ASSETS)]
    data['maturity_date'] = [d.strftime('%Y-%m-%d') for d in maturities]
    
    # Assign HQLA status logically
    is_hqla = []
    for p_type in data['product_type']:
        if p_type == 'G-Sec':
            is_hqla.append('Level 1')
        elif p_type == 'Corp Bond':
            is_hqla.append(np.random.choice(hqla_levels, p=[0, 0.7, 0.3])) # Corp bonds can be Level 2A or not HQLA
        else:
            is_hqla.append('No')
    data['is_hqla'] = is_hqla

    assets_df = pd.DataFrame(data)
    # For floating rate assets, repricing period can't be 0
    assets_df.loc[assets_df['rate_type'] == 'Fixed', 'repricing_period_days'] = 0
    return assets_df

def generate_liabilities():
    """Generates a DataFrame of pseudo bank liabilities."""
    liability_types = ['Savings', 'Current', 'Retail FD', 'Corporate FD']
    
    data = {
        'id': [f'LIAB_{i+1:04d}' for i in range(NUM_LIABILITIES)],
        'product_type': np.random.choice(liability_types, NUM_LIABILITIES, p=[0.4, 0.3, 0.2, 0.1]),
        'amount': np.round(np.random.uniform(0.01, 2.5, NUM_LIABILITIES), 2), # in INR Crores
        'interest_rate': np.round(np.random.uniform(2.5, 7.5, NUM_LIABILITIES), 2),
    }
    
    # Assign rate types and maturity dates logically
    rate_types = []
    maturities = []
    for p_type in data['product_type']:
        if p_type in ['Savings', 'Current']:
            rate_types.append('Floating')
            maturities.append(None) # Non-maturity deposits
        else: # This is a Fixed Deposit
            rate_types.append('Fixed')
            # --- THIS IS THE CORRECTED LOGIC ---
            random_days = np.random.uniform(15, 365 * 5)
            maturity_date = BASE_DATE + timedelta(days=int(random_days))
            maturities.append(maturity_date)

    data['rate_type'] = rate_types
    data['maturity_date'] = [d.strftime('%Y-%m-%d') if d else None for d in maturities]
    
    liabilities_df = pd.DataFrame(data)
    # Clean up interest rates for Current accounts (typically 0)
    liabilities_df.loc[liabilities_df['product_type'] == 'Current', 'interest_rate'] = 0
    # Add repricing period (simplified: all floating liabilities reprice daily)
    liabilities_df['repricing_period_days'] = 0
    liabilities_df.loc[liabilities_df['rate_type'] == 'Floating', 'repricing_period_days'] = 1

    return liabilities_df

# --- Main Execution ---
if __name__ == "__main__":
    print("Starting data generation for Indus National Bank...")
    create_directories()
    
    # Generate and save assets
    assets = generate_assets()
    assets.to_csv(ASSET_FILE, index=False)
    print(f"-> Successfully generated {len(assets)} asset records.")
    print(f"-> Saved assets to '{ASSET_FILE}'")

    # Generate and save liabilities
    liabilities = generate_liabilities()
    liabilities.to_csv(LIABILITY_FILE, index=False)
    print(f"-> Successfully generated {len(liabilities)} liability records.")
    print(f"-> Saved liabilities to '{LIABILITY_FILE}'")
    
    print("\nData generation complete.")