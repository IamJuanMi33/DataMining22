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

df = pd.read_csv('csv/death-rates-from-air-pollution.csv')
df.info()
print(f"\n---------------\n {df.isna()} \n---------------\n\n")

correct_df = df.copy()
correct_df.rename(columns={'Entity': 'Pais', 'Code': 'Clave', 'Year': 'Anio',
                           'Deaths - Air pollution - Sex: Both - Age: Age-standardized (Rate)': 'MpContaminacionAerea',
                           'Deaths - Household air pollution from solid fuels - Sex: Both - Age: Age-standardized (Rate)': 'MpContaminacionAireDomestico',
                           'Deaths - Ambient particulate matter pollution - Sex: Both - Age: Age-standardized (Rate)': 'MpContaminacionAmbiental',
                           'Deaths - Ambient ozone pollution - Sex: Both - Age: Age-standardized (Rate)': 'MpOzonoAmbiental'}, inplace=True)

print_tabulate(correct_df.head())
correct_df.to_csv(r'csv/death-rates-from-air-pollution-headers.csv', index=False)
