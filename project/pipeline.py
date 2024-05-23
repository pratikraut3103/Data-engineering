from kaggle.api.kaggle_api_extended import KaggleApi
import shutil
import os



def move_csv(current, destination):
    shutil.move(current, destination)

def rename_csv(old,new):
    os.rename(old,new)
def housing_data(data_path):
    api.dataset_download_file('yasserh/housing-prices-dataset', fr'Housing.csv', path=data_path)
    #move_csv(os.path.join(current_dir, 'Housing.csv'), os.path.join(data_path, 'Housing.csv'))

def economic_data(data_path):
    api.dataset_download_file('fernandol/countries-of-the-world', fr'countries of the world.csv',path=data_path)
    rename_csv(os.path.join(data_path, 'countries%20of%20the%20world.csv'), os.path.join(data_path, 'countries_economic.csv'))
    #move_csv(os.path.join(current_dir, 'countries_economic.csv'), os.path.join(data_path, 'countries_economic.csv'))

# Authenticate using kaggle.json
if __name__ == '__main__':
    api = KaggleApi()
    api.authenticate()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.abspath(os.path.join(current_dir, os.pardir))
    data_path = os.path.join(base_path, 'data')

    print(data_path)
    print(current_dir)
    housing_data(data_path)
    print('Housing data done')
    economic_data()
    print('Economic data done')
    print('Alas')


