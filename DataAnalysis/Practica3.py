from fileinput import filename
from statistics import mean
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

def analysis(file_name:str)-> None:
    df = pd.read_csv(file_name)

    dfList = ["MpContaminacionAerea", "MpContaminacionAireDomestico", "MpContaminacionAmbiental", "MpOzonoAmbiental"]
    df['TotaldeMuertes'] = df[dfList].sum(axis=1)

    print_tabulate(df.groupby(["Pais", "Anio"], as_index=False)[["TotaldeMuertes"]]
                    .aggregate(pd.DataFrame.sum).head())
    print("\n\n")

    print_tabulate(df.groupby(["Pais"], as_index=False)["MpContaminacionAerea"]
                    .agg(['min', 'max', 'mean', 'sum', 'var', 'std']).head())
    print("\n\n")

    print_tabulate(df.groupby(["Pais"], as_index=False)["MpContaminacionAireDomestico"]
                    .agg(['min', 'max', 'mean', 'sum', 'var', 'std']).head())
    print("\n\n")

    print_tabulate(df.groupby(["Pais"], as_index=False)["MpContaminacionAmbiental"]
                    .agg(['min', 'max', 'mean', 'sum', 'var', 'std']).head())
    print("\n\n")

    print_tabulate(df.groupby(["Pais"], as_index=False)["MpOzonoAmbiental"]
                    .agg(['min', 'max', 'mean', 'sum', 'var', 'std']).head())
    print("\n\n")

    print_tabulate(df.describe())
    print("\n\n")

    print(df.kurtosis(numeric_only=True))
    print("\n\n")

    print(df.skew(numeric_only=True))
    print("\n\n")

analysis("csv/death-rates-from-air-pollution-headers.csv")


