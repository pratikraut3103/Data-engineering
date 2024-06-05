from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import os
import zipfile
import sqlite3


def un_zip_file(source):
    with zipfile.ZipFile(f"{source}.zip", 'r') as zip_ref:
        zip_ref.extractall(source)

def rename_csv(old,new):
    os.rename(old,new)

def vehicle_sales_data(data_path, db_path):
    api.dataset_download_file('syedanwarafridi/vehicle-sales-data', fr'car_prices.csv', path=data_path)
    un_zip_file(os.path.join(data_path, 'car_prices.csv'))
    rename_csv(os.path.join(data_path, 'car_prices.csv'), os.path.join(data_path, 'Vehicle_sales_data.csv'))
    data = pd.read_csv(fr'{data_path}/Vehicle_sales_data.csv/car_prices.csv')
    data = data[["year", "state"]]
    cleaned_data = data.groupby('year').count()
    cleaned_data.rename(columns={"year": "Year", "state": "Number of Vehicles sold"}, inplace=True)
    cleaned_data.sort_values(by="year")
    conn = sqlite3.connect(db_path)
    cleaned_data.to_sql('Vehicle_sales_data', conn, index=False, if_exists='replace')


def co2_emission_data(data_path, db_path):
    api.dataset_download_file('soheiltehranipour/co2-dataset-in-usa', fr'co2.csv',path=data_path)
    rename_csv(os.path.join(data_path, 'co2.csv'), os.path.join(data_path, 'co2_emission.csv'))
    data = pd.read_csv(fr'{data_path}/co2_emission.csv')
    data["Year"] = data["YYYYMM"].astype(str).str[:4]
    data.drop(columns="YYYYMM", inplace=True)
    cleaned_data = data.groupby("Year").sum()
    conn = sqlite3.connect(db_path)
    cleaned_data.to_sql('co2_emission', conn, index=False, if_exists='replace')

# Authenticate using kaggle.json
if __name__ == '__main__':
    api = KaggleApi()
    api.authenticate()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.abspath(os.path.join(current_dir, os.pardir))
    data_path = os.path.join(base_path, 'data')
    database_file_path = os.path.join(data_path, 'database.csv')

    database_name = 'Data.sqlite'

    db_path = os.path.join(data_path, database_name)
    vehicle_sales_data(data_path,db_path)
    co2_emission_data(data_path,db_path)




