from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import os
import shutil
import sqlite3

def rename_csv(old,new):
    os.rename(old,new)
def housing_data(data_path, db_path):
    api.dataset_download_file('yasserh/housing-prices-dataset', fr'Housing.csv', path=data_path)
    data = pd.read_csv(fr'{data_path}/Housing.csv')
    print(data.head())
    conn = sqlite3.connect(db_path)
    data.to_sql('Housing_data', conn, index=False, if_exists='replace')


def economic_data(data_path, db_path):
    api.dataset_download_file('fernandol/countries-of-the-world', fr'countries of the world.csv',path=data_path)
    rename_csv(os.path.join(data_path, 'countries%20of%20the%20world.csv'), os.path.join(data_path, 'countries_economic.csv'))
    data = pd.read_csv(fr'{data_path}/countries_economic.csv')
    data = data.dropna(axis=0, how='any')
    conn = sqlite3.connect(db_path)
    data.to_sql('countries_economic', conn, index=False, if_exists='replace')

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

    print(data_path)
    print(current_dir)
    housing_data(data_path,db_path)
    print('Housing data done')
    economic_data(data_path,db_path)
    print('Economic data done',db_path)



