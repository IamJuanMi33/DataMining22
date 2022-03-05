import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_file('pavan9065/air-pollution', file_name='death-rates-from-air-pollution.csv')