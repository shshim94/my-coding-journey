
# Personal Finance Integration ETL Pipeline

# Project Structure

```
finance_etl_project/
├── etl_pipeline.py              # Main ETL script
├── data/
│   ├── bank.xlsx                # Bank transaction log (raw)
│   └── expense_data_1.csv       # User-entered expenses
├── output/
│   └── merged_transactions.csv  # Final enriched dataset
└── README.md
```

---

## Pipeline Overview

### Step 1: Extract
- Reads raw transaction data from `bank.xlsx`
- Loads categorized user expenses from `expense_data_1.csv`

### Step 2: Transform
- Standardizes dates and formats
- Adds (-) signs to expenses while keeping any income positive (+)
- Matches expenses to transactions by date (±1 day) and amount
- Flags matched vs unmatched transactions
- Enriches bank data with category, subcategory, and user notes

### Step 3: Load
- Saves a cleaned, structured output CSV to the `output/` folder
- Output is suitable for further analysis or dashboard integration

---

## 📊 Output Sample

| DATE       | TRANSACTION_DETAILS | AMOUNT | BALANCE_AMT | MATCHED_CATEGORY | IS_MATCHED |
|------------|----------------------|--------|--------------|------------------|------------|
| 2024-01-05 | Starbucks             | -500   | 1,950        | Food             | True       |
| 2024-01-06 | Salary                | 2500   | 4,450        | Income           | True       |
| 2024-01-07 | ATM Withdrawal        | -2000  | 2,450        | (Unmatched)      | False      |

---

## 🛠 Technologies Used

- Python 3.x
- pandas
- Jupyter/IDLE-compatible
- Excel + CSV support

---
