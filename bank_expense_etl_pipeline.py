import pandas as pd

# Step 1: Load bank and expense datasets

bank_df = pd.read_excel("data/bank.xlsx", sheet_name="Sheet1")

expense_df = pd.read_csv("data/expense_data_1.csv")

# Step 2: Clean date column

bank_df["DATE"] = pd.to_datetime(bank_df["DATE"], errors='coerce')

expense_df["Date"] = pd.to_datetime(expense_df["Date"], errors='coerce')

# Step 3: Clean column names

bank_df.columns = [col.strip().upper().replace(" ", "_") for col in bank_df.columns]

expense_df.columns = [col.strip().upper().replace(" ", "_") for col in expense_df.columns]

# Step 4: From bank transaction dataset, subtract deposit amount from withdrawal amount and create a new 'amount' column

bank_df["AMOUNT"] = bank_df["DEPOSIT_AMT"].fillna(0) - bank_df["WITHDRAWAL_AMT"].fillna(0)

# Step 5: From expense dataset, put (-) in front of expenses, and keep amount positive for income

expense_df["AMOUNT_NORMALIZED"] = expense_df.apply(
    lambda row: row["AMOUNT"] if row["INCOME/EXPENSE"].lower() == "income" else -abs(row["AMOUNT"]), axis=1
)

# Step 6: Round amount for easier matching of the bank transactions and expenses

bank_df["AMOUNT_ROUNDED"] = bank_df["AMOUNT"].round(0)
bank_df["DATE_MINUS1"] = bank_df["DATE"] - pd.Timedelta(days=1)
bank_df["DATE_PLUS1"] = bank_df["DATE"] + pd.Timedelta(days=1)

expense_df["AMOUNT_ROUNDED"] = expense_df["AMOUNT_NORMALIZED"].round(0)

# Step 7 Begin matching expense row with bank transactions
# Step 7-1: Create new columns to track matching

bank_df["MATCHED_EXPENSE_NOTE"] = None
bank_df["MATCHED_CATEGORY"] = None
bank_df["MATCHED_SUBCATEGORY"] = None

# Step 7-2: Match expense with bank transaction

for idx, exp_row in expense_df.iterrows():
    exp_amount = exp_row["AMOUNT_ROUNDED"]
    exp_date = exp_row["DATE"]

# Step 7-3: Look for bank transactions within +- 1 day of expense date and has the same amount with the expense

    match = bank_df[
        (bank_df["AMOUNT_ROUNDED"] == exp_amount) &
        (bank_df["DATE"] >= exp_date - pd.Timedelta(days=1)) &
        (bank_df["DATE"] <= exp_date + pd.Timedelta(days=1)) &
        # Match only expenses that have not been matched yet
        (bank_df["MATCHED_EXPENSE_NOTE"].isnull())
    ]
    # Update newly added column's data when matched
    if not match.empty:
        match_idx = match.index[0]
        bank_df.at[match_idx, "MATCHED_EXPENSE_NOTE"] = exp_row["NOTE"]
        bank_df.at[match_idx, "MATCHED_CATEGORY"] = exp_row["CATEGORY"]
        bank_df.at[match_idx, "MATCHED_SUBCATEGORY"] = exp_row["SUBCATEGORY"]

# Step 8: Indicate expenses that have been matched with transactions in the new column

bank_df["IS_MATCHED"] = bank_df["MATCHED_EXPENSE_NOTE"].notnull()

# Step 9: Remove columns that were used for the matching process, and thus no longer needed since the matching process is complete

columns_to_drop = ["AMOUNT_ROUNDED", "DATE_MINUS1", "DATE_PLUS1"]
cleaned_bank_df = bank_df.drop(columns=columns_to_drop, errors="ignore")

# Step 10: Reorganize column for better readbability

final_columns = [
    "DATE", "TRANSACTION_DETAILS", "AMOUNT", "BALANCE_AMT",
    "MATCHED_CATEGORY", "MATCHED_SUBCATEGORY", "MATCHED_EXPENSE_NOTE", "IS_MATCHED"
]

final_df = cleaned_bank_df[final_columns]

# Step 11: Export path

final_df.to_csv("/output/merged_transactions.csv", index=False)