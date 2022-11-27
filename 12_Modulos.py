# MODULOS
"""
Un modulo es un archivo que contiene un conjunto de codigo o un conjunto de funciones, que puede incluirse en una aplicacion.
Un modulo puede ser un archivo con una simple variable, una funcion o un gran codigo base.


# Para crear un modulo escribimos nuestro codigo en un script de Python y lo guardamos como un archivo .py

# Para importar un modulo, escribimos IMPORT y el nombre del archivo, sin .py

# Para importar varias funciones de un archivo se escribe FROM *archivo* IMPORT *funciones*

# Para cambiarles el nombre a las funciones, utilizamos AS

# Como en otros sistemas operativos, podemos importar modulos preestablecidos.
# Por ejemplo, math, datetime, os, sys, random, statistics, collections, json, re.

# Usando el modulo OS es posible ejecutar automaticamente varias funciones del sistema operativo. Provee las funciones
# para crear, modificar el directorio actual, y remover el directorio (archivo), tomar su contenido, cambiar e identificar
# el directorio actual.
import os
os.mkdir('Nombre_del_directorio') #Crear un directorio
os.chdir('ruta') #Cambiar el directorio actual
os.getcwd() #Directorio actual
os.rmdir() #Eliminar directorio

# El modulo SYS provee funciones y variables usadas para manipular diferentes partes del entorno de Python.
# sys.argv devuelve una lista de argumentos de linea de comandos enviadas a un script de Python. El item en el indice 0
# siempre sera el nombre del script.
import sys
sys.maxsize #Devuelve la variable integral mas grande que toma
sys.path #Saber la ruta de entorno
sys.version #La version de Python que se utiliza
sys.exit() #Salir de sys

# El modulo STATISTICS provee funciones para estadisticas matematicas de datos numericos. Las mas populares: MEAN, MEDIAN, MODE, STDEV, etc.
from statistics import * #Importar todo del modulo statistics
edades = [20, 20, 19, 3, 40, 20, 23, 25, 29]
print(mean(edades))
print(median(edades))
print(mode(edades))
print(stdev(edades))

# El modulo MATH incluye varias operaciones matematicas
import math
print(math.pi) #Constante PI
print(math.sqrt(16)) #Raiz cuadrada
print(math.pow(2, 3)) #Funcion exponencial (numero, exponente)
print(math.floor(9.81)) #Redondeo hacia abajo
print(math.ceil(9.81)) #Redondeo hacia arriba
print(math.log10(100)) #Logaritmo de base 10

# Modulo STRING
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# El modulo RANDOM permite arrojar un numero aleatorio entre 0 y 0.9999...
from random import *
print(random()) #Devuelve entre 0 y 0.9999
print(randint(5, 20)) #Devuelve un entero entre el primer y segundo numero inclusive
"""
#1. Write a function which generates a six digit/character random_user_id. 
import string, random
from typing import ForwardRef
def id_aleatorio():
    todo = string.ascii_letters + string.digits
    ID = str()
    for x in range(6): ID += random.choice(todo)
    return ID
 
#2. Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters
# and the second input is the number of IDs which are supposed to be generated.
def id_generado_por_usuario():
    caracteres = int(input('Caracteres: '))
    ids = int(input('IDs: '))
    todo = string.ascii_letters + string.digits
    for y in range(ids):
        ID = str()
        for x in range(caracteres): ID += random.choice(todo)
        else: print(ID)

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def generador_rgb():
    r = str(random.choice(range(0,255)))
    g = str(random.choice(range(0,255)))
    b = str(random.choice(range(0,255)))
    rgb = str('rgb('+ r +', ' + g + ', ' + b + ')')
    return rgb

#4. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9
# and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def lista_colores_hexadecimales():
    cantidad = random.randint(0, 10)
    lista = []
    for x in range(cantidad):
        lista.append('#')
        for y in range(6): lista[x] += random.choice(string.hexdigits)
    return lista

#5. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def generador_lista_rgb():
    cantidad = random.randint(1, 10)
    lista = []
    for x in range(cantidad):
        r = str(random.choice(range(0,255)))
        g = str(random.choice(range(0,255)))
        b = str(random.choice(range(0,255)))
        lista.append(str('rgb('+ r +', ' + g + ', ' + b + ')'))
    return lista

#6. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generar_colores(opc, cantidad):
    lista = []
    if opc == 'hexa':
        for x in range(cantidad):
            lista.append('#')
            for y in range(6): lista[x] += random.choice(string.hexdigits)
    else:
        for x in range(cantidad):
            r = str(random.choice(range(0,255)))
            g = str(random.choice(range(0,255)))
            b = str(random.choice(range(0,255)))
            lista.append(str('rgb('+ r +', ' + g + ', ' + b + ')'))
    return lista

#7. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def lista_aleatoria(lista):
    random.shuffle(lista)
    return lista

#8. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def siete_numeros():
    numeros = []
    while len(numeros) != 7:
        y = random.randint(0, 9)
        if y not in numeros: numeros.append(y)
    return numeros

