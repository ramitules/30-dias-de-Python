# PYTHON PACKAGE MANAGER

# PIP significa Prefered Installer Program. Utilizamos PIP para instalar diferentes paquetes Python.
# Un paquete es un modulo de Python que contiene uno o mas modulos, u otros paquetes.
# Un modulo o modulos que podamos instalar en nuestra aplicacion es un paquete. En programacion,
# no tenemos que escribir cada programa de utilidad; en su lugar, instalamos paquetes y los importamos.

#Instalar PIP
# En un terminal, escribir y ejecutar:	pip install pip
# Para chequear si esta instalado: pip --version

# Ahora chequearemos si tenemos instalados algunos paquetes populares en la comunidad de Python.

#Instalar paquetes con PIP
# Intentemos instalar numPy (numeric Python), uno de los paquetes mas populares en machine learning
# y data science.
# Numpy es el paquete fundamental para la computacion cientifica en Python. Contiene, entre otros:
#	Un poderoso objeto vector de N dimensiones
#	Funciones sofisticadas
#	Herramientas para integracion de C/C++ y Fortran
#	Algebra lineal, transformacion de Fourier, y capacidad para numeros aleatorios
# pip install numpy
import numpy

# Pandas es una libreria open source que contiene herramientas de alta performance y facil
# de usar para estructuras y analisis de datos.
# pip install pandas
import pandas

#Ahora importaremos un modulo de navegador web, que nos permite abrir cualquier pagina web.
# Este modulo ya viene preinstalado desde Python 3. Por ejemplo, si quisieramos abrir cualquier
# cantidad de paginas web en cualquier momento o quisieramos programar algo, el modulo webbrowser
# puede ser utilizado
import webbrowser
#lista_url = ['http://www.python.org',
#			 'http://www.facebook.com',
#			 'http://www.twitter.com']

#for url in lista_url:
#	webbrowser.open_new_tab(url)

#Se pueden eliminar paquetes con: pip uninstall paquete

#Para saber los paquetes instalados: pip list

#Para conocer informacion de un paquete: pip show paquete

# Para generar los paquetes necesarios en un proyecto e incluirlo en la lista de requerimientos,
# utilizamos pip freeze. Un archivo requirements.txt contiene todos los paquetes instalados en
# un proyecto Python.

#Leer desde una URL
# Hasta ahora sabemos como leer o escribir en un archivo local. A veces, necesitamos leer informacion
# desde una pagina web o una API (Application Program Interface). Es necesario intercambiar
# datos estructurados entre servidores, generalmente como datos JSON. Para abrir una conexion,
# necesitamos un paquete llamado REQUESTS, el cual nos permite abrir una conexion e implementar 
# operaciones CRUD (crear, leer, actualizar y eliminar): pip install requests
#	get(): abrir una red y capturar datos desde una url - devuelve un objeto
#	status_code: luego de capturar datos, podemos chequear el estado de la operacion
#	headers: chequear el tipo de cabeceras
#	text: extraer texto del objeto capturado
#	json: extraer datos JSON

#Crear un paquete
# Un modulo puede contener diferentes objetos, como clases, funciones, etc.
# Un paquete puede contener uno o varios modulos. Un paquete es, en realidad, una carpeta que
# contiene uno o varios archivos de modulos. Vamos a crear un paquete llamado 'mipaquete'
# Primero, crear una carpeta llamado 'mipaquete'
# Luego, crear un archivo vacio 'init.py' dentro de la carpeta y los modulos a utilizar
# Ahora, a importar el paquete
from mipaquete import aritmetica

print(aritmetica.anadir_numeros(1, 2, 3, 4, 5))

from mipaquete import bienvenida

print(bienvenida.bienvenida_persona('Ramiro', 'Tules'))

# Aqui se pudo ver que el paquete funciono perfectamente. La carpeta contiene un archivo especial
# llamado init.py, este contiene el contenido del paquete, y asi Python puede reconocerlo como tal.
# El archivo init.py contiene recursos especiales de sus modulos para que lo podamos importar en 
# otros archivos Python.

#Otros paquetes esenciales
# Bases de datos
#	SQLAlchemy o SQLObject - acceso orientado a objetos a diferentes sistemas de base
#	de datos: pip install SQLAlchemy
# Desarrollo web
#	Django - framework web avanzado: pip install django
#	Flask - pequeño framework para Python basado en Werkzeug, Jinja 2: pip install flask
# Analisis HTML
#	Beautiful Soup - Analisis HTML/XML diseñado para proyectos rapidos como screen-scraping.
#	pip install beautifulsoup4
#	PyQuery - implementa jQuery en Python; mas rapido que BeautifulSoup.
# Procesado XML
#	ElementTree - simple pero flexible contenedor de objetos, diseñado para almacenar
#	estructuras de datos jerarquicamente. A partir de Python 2.5 ya viene preinstalado.
# GUI
#	PyQt
#	TkInter - interfaz de usuario tradicional para Python
# Data Analysis, Data Science y Machine Learning
#	Numpy
#	Pandas
#	SciPy - libreria de machine learning. Contiene modulos para optimizacion, algebra lineal,
#	integracion, procesamiento de imagenes y estadistica
#	Scikit-Learn: considerada una de las mejores librerias para trabajar con datos compeljos.
#	Como una combinacion de Numpy y SciPy
#	TensorFlow - libreria de machine learning desarrollada por Google
#	Keras - considerada una de las mejores librerias de machine learning en Python. Provee
#	un mecanismo sencillo para expresar redes neuronales. Keras provee ademas una de las mejores
#	utilidades para compilar modelos, procesar sets de datos, visualizacion de graficos, y mucho mas
# Redes
#	Requests - es un paquete que podemos utilizar para enviar pedidos (requests) a un servidor.

#1. Read this url and find the 10 most frequent words. 'http://www.gutenberg.org/files/1112/1112.txt'
url = 'http://www.gutenberg.org/files/1112/1112.txt'

import requests
texto = requests.get(url).text
palabras = set(texto.split())
lista_palabras = texto.split()
contadores = []
for palabra in palabras:
	contador = lista_palabras.count(palabra)
	contadores.append([contador, palabra])
contadores.sort(reverse = True)
for i in range(10): print(contadores[i])

#2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
#   the min, max, mean, median, standard deviation of cats' weight in metric units.
#   the min, max, mean, median, standard deviation of cats' lifespan in years.
#   create a frequency table of country and breed of cats.

#3. UCI is one of the most common places to get data sets for data science and machine learning.
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional
# libraries it will be difficult, so you may try it with BeautifulSoup4