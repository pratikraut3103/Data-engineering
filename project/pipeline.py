from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate using kaggle.json
if __name__ == '__main__':
    api = KaggleApi()
    api.authenticate()
    #api.dataset_download_file('fernandol/countries-of-the-world',fr'countries of the world.csv')
    api.dataset_download_file('competitions/house-prices-advanced-regression-techniques', fr'test.csv')