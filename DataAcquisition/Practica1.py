import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

api = KaggleApi()
api.authenticate()

api.dataset_download_file('pavan9065/air-pollution', file_name='death-rates-from-air-pollution.csv')

df = pd.read_csv('death-rates-from-air-pollution.csv')
print_tabulate(df.head())