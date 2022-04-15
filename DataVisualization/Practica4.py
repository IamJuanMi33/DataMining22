import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import plotly.express as px

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def visualization(file_name:str)-> None:
    df = pd.read_csv(file_name)

    # Total Deaths Column
    dfList = ["MpContaminacionAerea", "MpContaminacionAireDomestico", "MpContaminacionAmbiental", "MpOzonoAmbiental"]
    df['TotaldeMuertes'] = df[dfList].sum(axis=1)
    df_total = df.groupby(["Pais"], as_index=False)["TotaldeMuertes"].aggregate(pd.DataFrame.sum)

    # DF - Sum of all deaths
    deaths_vals = [(df["MpContaminacionAerea"].sum(axis= 0)), (df["MpContaminacionAireDomestico"].sum(axis= 0)),
                   (df["MpContaminacionAmbiental"].sum(axis= 0)), (df["MpOzonoAmbiental"].sum(axis= 0))]
            
    deaths_df = pd.DataFrame(deaths_vals, columns=['TotaldeMuertes'])


    # Line graph - Muertes por Año
    df_anios = df.groupby(["Anio"], as_index=False)["TotaldeMuertes"].aggregate(pd.DataFrame.sum)
    df_anios.plot("Anio", "TotaldeMuertes", color='orange', marker='o', title="Muertes por contaminación por año (Global)", legend=False, grid=True)
    plt.xlabel("Año")
    plt.ylabel("Número de Muertes")
    plt.savefig("img/MuertesxAnio.png")
    plt.close()

    # Bar graph - Muertes totales por País
    df_total.plot.bar(x="Pais", y="TotaldeMuertes", figsize=(60,40), legend=False, grid=True)    
    plt.title("Total de Muertes por País", fontsize=80)
    plt.xticks(rotation=90) 
    plt.xlabel('País', fontsize=50)
    plt.ylabel('Número de Muertes', fontsize=50)
    plt.savefig("img/MuertesxPais.png")
    plt.close()

    # Box&Whiskers graph - Muertes totales por País (Con outliers)
    df_total.plot.box()
    plt.savefig("img/BoxMuertesxPais.png")
    plt.close()

    # Pie graph - Muertes por Contaminación en general (Global)  
    deaths_df.plot.pie(y='TotaldeMuertes', figsize=(9, 7), title="Total de Muertes por Contaminación (Global)", labels=['','','',''], autopct='%.2f')
    plt.legend(['Contaminación Aérea', 'Contaminación Aire Doméstico',
                'Contaminación Ambiental', 'Ozono Ambiental'])
    plt.ylabel("")
    plt.savefig("img/PieMuertes.png")
    plt.close()

    # World graph - Muertes totales por País
    df_total_countries = df.groupby(["Pais", "Clave"], as_index=False)["TotaldeMuertes"].aggregate(pd.DataFrame.sum)
    fig = px.choropleth(df_total_countries, locations="Clave", color="TotaldeMuertes", hover_name="Pais", title="Muertes Totales por País")
    fig.show()

visualization("csv/death-rates-from-air-pollution-headers.csv")