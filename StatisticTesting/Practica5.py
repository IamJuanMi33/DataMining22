import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def stat_test(file_name:str)-> None:

    df = pd.read_csv(file_name)

    # Total Deaths Column
    dfList = ["MpContaminacionAerea", "MpContaminacionAireDomestico", "MpContaminacionAmbiental", "MpOzonoAmbiental"]
    df['TotaldeMuertes'] = df[dfList].sum(axis=1)
    df_total = df.groupby(["Pais"], as_index=False)["TotaldeMuertes"].aggregate(pd.DataFrame.sum)

    # DF - Sum of all deaths
    deaths_vals = [(df["MpContaminacionAerea"].sum(axis= 0)), (df["MpContaminacionAireDomestico"].sum(axis= 0)),
                   (df["MpContaminacionAmbiental"].sum(axis= 0)), (df["MpOzonoAmbiental"].sum(axis= 0))]
        
    deaths_df = pd.DataFrame(deaths_vals, columns=['TotaldeMuertes'])

     # DF - Deaths per Country
    df_total_countries = df.groupby(["Pais", "Clave"], as_index=False)["TotaldeMuertes"].aggregate(pd.DataFrame.sum)

    # DF - Deaths per Year
    df_anios = df.groupby(["Anio"], as_index=False)["TotaldeMuertes"].aggregate(pd.DataFrame.sum)


    # ANOVA AÑOS
    mod = ols('TotaldeMuertes ~ Anio', data=df_anios).fit()
    aov_table_anio = sm.stats.anova_lm(mod, typ=2)
    print(aov_table_anio)


stat_test("csv/death-rates-from-air-pollution-headers.csv")