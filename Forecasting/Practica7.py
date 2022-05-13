import numbers
from typing import Dict, Tuple
import pandas as pd
import matplotlib.pyplot as plt
from requests import head
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

def linearRegression(df: pd.DataFrame, x: str, y: str)->Dict[str, float]:
    # Por si acaso ---------------
    fixed_x = transform_var(df, x)
    # ----------------------------
    model = sm.OLS(df[y], sm.add_constant(fixed_x), alpha=0.1).fit()
    bands = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]
    print_tabulate(pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0])
    coef = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]['coef']
    r_2_t = pd.read_html(model.summary().tables[0].as_html(),header=None,index_col=None)[0]
    return {'m': coef.values[1], 'b': coef.values[0], 'r2': r_2_t.values[0][3], 'r2_adj': r_2_t.values[1][3], 'low_band': bands['[0.025'][0], 'hi_band': bands['0.975]'][0]}

def plt_lr(df: pd.DataFrame, x:str, y:str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float, colors: Tuple[str, str]):
    fixed_x = transform_var(df, x)    
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[m * x + b for _, x in fixed_x.items()], color=colors[0])
    plt.fill_between(df[x],
                    [ m * x + low_band for _, x in fixed_x.items()],
                    [ m * x + hi_band for _, x in fixed_x.items()], alpha=0.2, color=colors[1])

df = pd.read_csv("csv/death-rates-from-air-pollution-headers.csv")

dfList = ["MpContaminacionAerea", "MpContaminacionAireDomestico", "MpContaminacionAmbiental", "MpOzonoAmbiental"]
df['TotaldeMuertes'] = df[dfList].sum(axis=1)


# Lr - Total Deaths per Year
df_anios = df.groupby(["Anio"], as_index=False)[["TotaldeMuertes"]].aggregate(pd.DataFrame.mean)
print("\n\n\t\t\t ----- TotaldeMuertes ----- ")
a = linearRegression(df_anios, "Anio", "TotaldeMuertes")
plt_lr(df=df_anios, x="Anio", y="TotaldeMuertes", colors=('red', 'orange'), **a)

plt.xticks(rotation=90)
plt.savefig('img/lr_TotalMuertes_Anio.png')
plt.close() 

# --- Para revisar cada una de las muertes consideradas con respecto a los años ---
# Lr - Deaths per Air pollution    
df_MPCA = df.groupby(["Anio"], as_index=False)["MpContaminacionAerea"].aggregate(pd.DataFrame.mean)
print("\n\n\t\t\t ----- MpContaminacionAerea ----- ")
b = linearRegression(df_MPCA, "Anio", "MpContaminacionAerea")
plt_lr(df=df_MPCA, x="Anio", y="MpContaminacionAerea", colors=('red', 'orange'), **b)

plt.xticks(rotation=90)
plt.savefig('img/lr_ContAerea_Anio.png')
plt.close() 

# Lr - Deaths per Household Air pollution
df_MPAD = df.groupby(["Anio"], as_index=False)["MpContaminacionAireDomestico"].aggregate(pd.DataFrame.mean)
print("\n\n\t\t\t ----- MpContaminacionAireDomestico ----- ")
c = linearRegression(df_MPAD, "Anio", "MpContaminacionAireDomestico")
plt_lr(df=df_MPAD, x="Anio", y="MpContaminacionAireDomestico", colors=('red', 'orange'), **c)

plt.xticks(rotation=90)
plt.savefig('img/lr_ContDomestico_Anio.png')
plt.close() 

# Lr - Deaths per Ambient pollution
df_MPCAl = df.groupby(["Anio"], as_index=False)["MpContaminacionAmbiental"].aggregate(pd.DataFrame.mean)
print("\n\n\t\t\t ----- MpContaminacionAmbiental ----- ")
d = linearRegression(df_MPCAl, "Anio", "MpContaminacionAmbiental")
plt_lr(df=df_MPCAl, x="Anio", y="MpContaminacionAmbiental", colors=('red', 'orange'), **d)

plt.xticks(rotation=90)
plt.savefig('img/lr_ContAmb_Anio.png')
plt.close() 

# Lr - Deaths per Ambient ozone
df_MPOA = df.groupby(["Anio"], as_index=False)["MpOzonoAmbiental"].aggregate(pd.DataFrame.mean)
print("\n\n\t\t\t ----- MpOzonoAmbiental -----")
e = linearRegression(df_MPOA, "Anio", "MpOzonoAmbiental")
plt_lr(df=df_MPOA, x="Anio", y="MpOzonoAmbiental", colors=('red', 'orange'), **e)

plt.xticks(rotation=90)
plt.savefig('img/lr_OzoAmb_Anio.png')
plt.close() 