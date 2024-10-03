# DataMining22
Este repositorio contiene un conjunto de scripts en Python diseñados para realizar tareas completas de minería de datos, utilizando las bibliotecas **pandas** y **numpy** como base para la manipulación de datos. El toolkit incluye scripts para adquirir, limpiar, analizar y visualizar datos, así como para realizar pruebas estadísticas, modelado lineal, predicciones, clasificación y clustering. Todo el proceso está optimizado para facilitar el análisis de datos de manera eficiente y escalable.

## Funcionalidades Principales
* Adquisición de datos: Scripts para obtener datos desde diversas fuentes (archivos CSV, Excel, bases de datos) utilizando pandas para estructurar los datos de manera eficiente.
* Limpieza de datos: Herramientas para limpiar, transformar y manejar datos faltantes, duplicados o inconsistentes, utilizando las capacidades avanzadas de pandas.
* Análisis de datos: Scripts para realizar análisis exploratorio y estadístico con pandas, identificando patrones y tendencias en los datos.
* Visualización de datos: Visualización de datos utilizando bibliotecas como Matplotlib y Seaborn para generar gráficos claros y comprensibles.
* Testing estadístico: Scripts para realizar pruebas estadísticas como t-tests, ANOVA y correlaciones, validando hipótesis sobre los datos.
* Modelado lineal: Herramientas para construir y evaluar modelos lineales (regresión lineal) y analizar su rendimiento.
* Predicciones y clasificación: Implementación de algoritmos de machine learning para hacer predicciones y clasificar datos, utilizando bibliotecas como Statmodels y numpy.
* Clustering: Aplicación de técnicas de clustering (agrupamiento) para segmentar datos en grupos significativos, como K-Means.

### Adquisición de la información
Como primer paso, es escencial definir qué es lo que se va a analizar y de dónde obtendremos esta información. En este caso se trabajó con una Base de Datos sobre la contaminación aérea en diferentes países. Además, esta Base de Datos se obtuvo del sitio web de [Kaggle](https://www.kaggle.com/), una página muy conocida en el mundo de la minería de datos. A continuación se puede visualizar las funciones utilizadas y la llamada a la API de Kaggle:
```
api = KaggleApi()
api.authenticate()

api.dataset_download_file('pavan9065/air-pollution', file_name='death-rates-from-air-pollution.csv')

df = pd.read_csv('death-rates-from-air-pollution.csv')
print_tabulate(df.head())
```

##
Este Toolkit para Minería de Datos brinda una solución para analizar de datos y funciona para desarrolladores que buscan realizar un proceso completo en el campo de la minería de datos, desde la adquisición hasta el modelado y las predicciones. Con una potente combinación de pandas y otras bibliotecas líderes en ciencia de datos, este toolkit te proporciona todas las herramientas necesarias para extraer valor significativo de los datos.


  
