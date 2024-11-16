"""
Pandas es una libreria de codigo abierto, de alta performance y facil de usar, capaz de trabajar con
estructuras de datos para realizar analisis. Pandas anade estructuras y herramientas disenadas para trabajar con
datos tipo tabla, los cuales son SERIES y DATA FRAMES. Provee herramientas para:
* Reformar
* Unir
* Ordenar
* Dividir
* Agregar
* Imputar

Una SERIE es una columna (como un vector), y un DataFrame es una tabla multidimensional compuesta por un conjunto
de series. Para crear una serie, basta con un vector de Numpy o una lista de Python
"""

import pandas as pd
import numpy as np

nums = [1, 2, 3, 4]
serie = pd.Series(nums)  # Serie con indices default
print(serie)
"""
0   1
1   2
2   3
3   4
dtype: int64
"""
serie = pd.Series(nums, index=[1, 2, 3, 4])  # Serie con indices personalizados
print(serie)
"""
1   1
2   2
3   3
4   4
dtype: int64
"""
frutas = ['Manzana', 'Naranja', 'Mango']
serie = pd.Series(frutas, index=[1, 2, 3])
print(serie)
"""
1   Manzana
2   Naranja
3   Mango
dtype: object
"""
yo = {
    'nombre': 'Ramiro',
    'pais': 'Argentina',
    'provincia': 'Buenos Aires'
}
serie = pd.Series(yo)  # Serie desde un diccionario
print(serie)
"""
nombre      Ramiro
pais        Argentina
provincia   Buenos Aires
dtype: object
"""
serie = pd.Series(10, index=[1, 2, 3, 4])  # Serie constante
print(serie)
"""
1   10
2   10
3   10
4   10
dtype: int64
"""
serie = pd.Series(np.linspace(5, 20, 10))
print(serie)
"""
0     5.000000
1     6.666667
2     8.333333
3    10.000000
4    11.666667
5    13.333333
6    15.000000
7    16.666667
8    18.333333
9    20.000000
dtype: float64
"""
# DataFrames
# Dataframe desde una lista de listas
datos = [
    ['Ramiro', 'Argentina', 'Buenos Aires'],
    ['Alexander', 'Colombia', 'Medellin'],
    ['Megan', 'Estados Unidos', 'North Carolina']
]
dataframe = pd.DataFrame(datos, columns=['Nombre', 'Pais', 'Provincia'])
print(dataframe)
"""
      Nombre            Pais           Provincia
0     Ramiro       Argentina        Buenos Aires
1  Alexander        Colombia            Medellin
2      Megan  Estados Unidos  Carolina del Norte
"""
# Dataframe desde una lista de diccionarios
datos = [
    {
        'nombre': 'Ramiro',
        'pais': 'Argentina',
        'provincia': 'Buenos Aires'
    }, {
        'nombre': 'Alexander',
        'pais': 'Colombia',
        'provincia': 'Medellin'
    }, {
        'nombre': 'Megan',
        'pais': 'Estados Unidos',
        'provincia': 'North Carolina'
    }
]
df_gente = pd.DataFrame(datos)
print(df_gente)
"""
MISMO RESULTADO
"""

# Leer CSV
dataframe = pd.read_csv('weight-height.csv')

print(dataframe)
print(dataframe.head())  # Mostrar las primeras 5 filas. Puede pasarse un argumento de X cantidad de filas
print(dataframe.tail())  # Mostrar las ultimas 5 filas. Puede pasarse un argumento de X cantida de filas
print(dataframe.shape)   # Tupla con la cantidad de filas y la cantidad de columnas
print(dataframe.columns)  # Todas las columnas
print(dataframe['Height'])  # Solo la columna "Height" como una serie. Se utiliza la key o nombre de la columna
print(dataframe['Height'].describe())  # Informacion estadistica de las alturas
print(dataframe.describe())  # Informacion estadistica del dataframe
print(dataframe.info())  # Informacion mas general del dataframe

# Anadir columna
pesos = [74, 78, 65]
alturas = [173, 175, 169]
df_gente['peso'] = pesos
df_gente['altura'] = alturas
print(df_gente)

# Modificar la altura de centimetros a metros
df_gente['altura'] = df_gente['altura'] / 100
print(df_gente)

# Calcular masa corporal (peso dividido altura al cuadrado)
df_gente['masa'] = df_gente['peso'] / (df_gente['altura'] * df_gente['altura'])
print(df_gente)

# Redondeo de la masa corporal a un solo digito
df_gente['masa'] = round(df_gente['masa'], 1)
print(df_gente)

# Agregar el ano de nacimiento
anos = ['1997', '1990', '1991']
df_gente['nacimiento'] = anos
df_gente['ano actual'] = pd.Series(2024, index=[0, 1, 2])
print(df_gente)
print(df_gente.peso.dtype)  # int64

# Cambiar tipo de dato
df_gente['nacimiento'] = df_gente['nacimiento'].astype('int')
print(df_gente.nacimiento.dtype)  # int32

# Agregar columna de anos
anos = df_gente['ano actual'] - df_gente['nacimiento']
df_gente['anos'] = anos

# Busqueda a traves de indice booleano
print(df_gente[df_gente['anos'] < 30])

