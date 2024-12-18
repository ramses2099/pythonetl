import os
from time import time

import pandas as pd
from sqlalchemy import exc

from config import DATA_FOLDER
from db_connection import connect_to_db, test_connect_to_db


def load_data(file_path: str) -> pd.DataFrame:
    # Load data from the given file path
    df = pd.read_csv(file_path)
    print(f"Data extracted successfully from file: {file_path}")
    return df


def transform_data(df) -> pd.DataFrame:
    # Transform the data
    # 'Date', 'Product_Category', 'Price', 'Discount', 'Customer_Segment',
    # 'Marketing_Spend', 'Units_Sold'
    sub_total = df["Price"] * df["Units_Sold"]
    descount = df["Discount"] / 100
    df["Total"] = sub_total + descount
    return df


def load_data_to_sql(df, engine)->None:
    try:
        start_time = time()
        # Load the transformed data into the database
        df.to_sql("EcommerceSales", engine, if_exists="append", index=False)
        end_time = time()
        print(f"Loading data time durations {round(end_time-start_time,2)}")
    except exc.SQLAlchemyError as e:
        print(f"An error occurred while loading data to SQL: {e}")
    
    print(f"Data loaded successfully to SQL table: EcommerceSales")


def elt_pipeline():
    # engine = connect_to_db()
    for file_name in os.listdir(DATA_FOLDER):
        if file_name.endswith(".csv"):
            data_file_path = f"{DATA_FOLDER}{file_name}"
            # Extract data from the file
            df = load_data(data_file_path)
            # Transform the data
            df = transform_data(df)
            # Create engine
            engine = connect_to_db()
            # If engine is None, then connection failed and exit the program
            if engine is None:
                print("Failed to connect to the database. Exiting the program.")
                return

            # Load the transformed data into the database
            load_data_to_sql(df, engine)            
            # print(df.head(5))


def main() -> None:
    os.system("cls")
    elt_pipeline()
    # test_connect_to_db()
    


if __name__ == "__main__":
    main()
