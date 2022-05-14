from statistics import mode
from typing import Dict, List, Tuple
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def classification(row, col):
    if row[col] < 150:
        return 1
    elif row[col] < 200:
        return 2
    return 3

def scatter_group_by(file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str):
    colors = ["blue", "gray", "red"]
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    
    for i, label in list(enumerate(labels)):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=colors[i])

    plt.title("Relacion entre muertes por año")
    plt.xlabel("Año")
    plt.ylabel("Muertes")
    ax.legend()
    plt.savefig(file_path)
    plt.close()

def euclidean_distance(p_1, p_2)->float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

def k_nearest_neighbors(points, labels, input_data, k):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        mode([labels[index] for index in point_nearest])
        for point_nearest in points_k_nearest
    ]

df = pd.read_csv("csv/death-rates-from-air-pollution-headers.csv")
dfList = ["MpContaminacionAerea", "MpContaminacionAireDomestico", "MpContaminacionAmbiental", "MpOzonoAmbiental"]
df['TotaldeMuertes'] = df[dfList].sum(axis=1)
df_anios = df.groupby(["Anio"], as_index=False)[["TotaldeMuertes"]].aggregate(pd.DataFrame.mean)
df_anios['Grupo'] = df_anios.apply(lambda row: classification(row, 'TotaldeMuertes'), axis=1)

plt.scatter(df_anios['Anio'], df_anios['TotaldeMuertes'])
plt.title("Relacion entre muertes por año")
plt.xlabel("Año")
plt.ylabel("Muertes")
plt.savefig("img/Relationship Y-TD.png")
plt.close()

scatter_group_by("img/groups.png", df_anios, "Anio", "TotaldeMuertes", "Grupo")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df_anios.itertuples(index=False, name=None)
]

points = [point for point, _ in list_t]
labels = [label for _, label in list_t]

kn = k_nearest_neighbors(
    points,
    labels,
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5,
)

print(kn)