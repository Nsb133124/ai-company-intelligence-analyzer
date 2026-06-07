import pandas as pd
import os

def save_company(company_data):

    file_name = "data/company_database.csv"

    new_row = pd.DataFrame([company_data])

    if os.path.exists(file_name):

        existing_df = pd.read_csv(file_name)

        updated_df = pd.concat(
            [existing_df, new_row],
            ignore_index=True
        )

        updated_df.to_csv(
            file_name,
            index=False
        )

    else:

        new_row.to_csv(
            file_name,
            index=False
        )

    print(f"Saved to {file_name}")
    print("Current Directory:", os.getcwd())