import numbers
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def transform_var(df: pd.DataFrame, x: str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x]
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linearRegression(df: pd.DataFrame, x: str, y: str)->None:
    # Por si acaso ---------------
    fixed_x = transform_var(df, x)
    # ----------------------------
    model = sm.OLS(df[y], sm.add_constant(fixed_x)).fit()
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='green')
    plt.plot(df_anios[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.savefig(f'img/lr_{y}_{x}.png')
    plt.close()
    # Regression Model 1

df1 = pd.read_csv("csv/death-rates-from-air-pollution-headers.csv")

dfList = ["MpContaminacionAerea", "MpContaminacionAireDomestico", "MpContaminacionAmbiental", "MpOzonoAmbiental"]
df1['TotaldeMuertes'] = df1[dfList].sum(axis=1)

# Lr - Total Deaths per Year

df_anios = df1.groupby(["Anio"], as_index=False)[["TotaldeMuertes"]].aggregate(pd.DataFrame.mean)
print("\n\n\t\t\t ----- TotaldeMuertes ----- ")
# print_tabulate(df_anios)
linearRegression(df_anios, "Anio", "TotaldeMuertes")

# --- Para revisar cada una de las muertes consideradas con respecto a los años ---
    
# Lr - Deaths per Air pollution    
df_MPCA = df1.groupby(["Anio"], as_index=False)["MpContaminacionAerea"].aggregate(pd.DataFrame.mean)
print("\n\n\t\t\t ----- MpContaminacionAerea ----- ")
linearRegression(df_MPCA, "Anio", "MpContaminacionAerea")

# Lr - Deaths per Household Air pollution
df_MPAD = df1.groupby(["Anio"], as_index=False)["MpContaminacionAireDomestico"].aggregate(pd.DataFrame.mean)
print("\n\n\t\t\t ----- MpContaminacionAireDomestico ----- ")
linearRegression(df_MPAD, "Anio", "MpContaminacionAireDomestico")

# Lr - Deaths per Ambient pollution
df_MPCAl = df1.groupby(["Anio"], as_index=False)["MpContaminacionAmbiental"].aggregate(pd.DataFrame.mean)
print("\n\n\t\t\t ----- MpContaminacionAmbiental ----- ")
linearRegression(df_MPCAl, "Anio", "MpContaminacionAmbiental")

# Lr - Deaths per Ambient ozone
df_MPOA = df1.groupby(["Anio"], as_index=False)["MpOzonoAmbiental"].aggregate(pd.DataFrame.mean)
print("\n\n\t\t\t ----- MpOzonoAmbiental -----")
linearRegression(df_MPOA, "Anio", "MpOzonoAmbiental")
