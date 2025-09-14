# Data Contract (v1)

Files:
- customers.csv — one row per customer
- loans.csv — one row per loan
- payments.csv — one row per billed EMI/payment attempt

Keys:
- customers.customer_id (PK)
- loans.loan_id (PK), loans.customer_id → customers.customer_id (FK)
- payments.payment_id (PK), payments.loan_id → loans.loan_id (FK)

Dates are ISO-8601 (YYYY-MM-DD). Amounts are decimals.
