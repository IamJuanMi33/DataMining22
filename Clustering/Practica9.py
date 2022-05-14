from statistics import mode
from typing import Dict, List, Tuple
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
from functools import reduce
from scipy.stats import mode

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

    for i, label in enumerate(labels):
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

def k_means(points: List[np.array], k: int):
    DIM = len(points[0])
    N = len(points)
    num_cluster = k
    iterations = 15

    x = np.array(points)
    y = np.random.randint(0, num_cluster, N)

    mean = np.zeros((num_cluster, DIM))
    for t in range(iterations):
        for k in range(num_cluster):
            mean[k] = np.mean(x[y == k], axis = 0)

        for i in range(N):
            dist = np.sum((mean - x[i]) ** 2, axis=1)
            pred = np.argmin(dist)
            y[i] = pred

    for kl in range(num_cluster):
        xp = x[y == kl, 0]
        yp = x[y == kl, 0]
        plt.scatter(xp, yp)

    plt.savefig("img/kmeans.png")
    plt.close()
    return mean

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

kn = k_means(
    points,
    3,
)

print(kn)