from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1] / "data" / "synthetic"
customers = pd.read_csv(root / "customers.csv")
loans = pd.read_csv(root / "loans.csv")
payments = pd.read_csv(root / "payments.csv")

print(customers.head(), "\n")
print(loans.head(), "\n")
print(payments.head(), "\n")

# Basic integrity checks
assert customers['customer_id'].is_unique
assert loans['loan_id'].is_unique
assert set(loans['customer_id']).issubset(set(customers['customer_id']))
assert set(payments['loan_id']).issubset(set(loans['loan_id']))
print("Basic integrity checks passed.")
