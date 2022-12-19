# MANIPULACION DE ARCHIVOS

# Hasta ahora hemos visto diferentes tipos de datos en Python. Generalmente guardamos los datos en distintos
# formatos de archivos. Ademas de manipular archivos, veremos distintos formatos de archivos (.txt, .json, 
# .xml, .csv, .tsv, .xlsx) en esta seccion. Primero, familiaricemonos con los tipos comunes de archivos (.txt).

# Manipulacion de archivos es una parte importada de la programacion que nos permite crear, leer, actualizar
# y eliminar archivos. En Python, para manipular archivos utilizamos la funcion OPEN('nombre_archivo', modo)

# MODOS
#   r: Read. Valor por defecto. Lee un archivo en modo lectura. Retorna error si no existe.
#   a: Append. Abre el archivo para añadir un registro. Crea el archivo si no lo encuentra.
#   w: Write. Abre el archivo para escritura. Crea el archivo si no lo encuentra. Sobreescribe archivos existentes.
#   x: Create. Crea el archivo. Retorna error si el archivo existe.
#   t: Text. Valor por defecto. Modo texto.
#   b: Binary. Modo binario (por ejemplo, imagenes).

f = open('ejemplo.txt')
print(f) # <_io.TextIOWrapper name='ejemplo.txt' mode='r' encoding='cp1252'>
# En el ejemplo anterior, se imprime informacion del archivo. Tenemos diferentes formas de abrir
# archivos: READ(), READLINE, READLINES. El archivo abierto debe cerrarse con .close().

# read(): Lee todo el texto como un string. Si queremos limitar la cantidad de caracteres, podemos
# poner un entero en el metodo (read(int))

texto = f.read()
print(type(texto))
print(texto)
f.close()

f = open('ejemplo.txt')
texto_corto = f.read(10)
print(texto_corto)
f.close()

#readline(): Lee la primer linea.
f = open('ejemplo.txt')
linea = f.readline()
print(linea)
f.close()

#readlines(): Lee el texto linea a linea y las retorna en una lista
f = open('ejemplo.txt')
lineas = f.readlines()
print(lineas)
f.close()

#splitlines(): Lee el texto linea a linea y las retorna en una lista, sin caracteres de saltos de linea
f = open('ejemplo.txt')
lineas2 = f.read().splitlines()
print(lineas2)
f.close()

#Para no olvidarnos de cerrar los archivos, podemos abrirlos con WITH para que se cierren solos.
with open('ejemplo.txt') as f:
    lineas3 = f.read().splitlines()
    print(lineas3)

#Escribir sobre un archivo existente
with open('ejemplo.txt', 'a') as f:
    f.write('Este texto se agrega al final')

with open('ejemplo.txt', 'w') as f:
    f.write('Este texto se escribira en un archivo nuevo, sobreescribiendo al anterior')

#Si queremos eliminar un archivo, utilizamos el modulo OS

import os
#os.remove('ejemplo.txt')
#Si no encuentra el archivo, arroja error. Por ende es importante utilizar una condicion

#if os.path.exists('ejemplo.txt'):
#    os.remove('ejemplo.txt')
#else:
#    print('El archivo no existe')

#Archivo JSON: JavaScript Object Notation. Es un objeto Javascript hecho string, o un diccionario en Python.
#Diccionario
diccionario_persona = {
    "nombre" : "Ramiro",
    "pais" : "Argentina",
    "provincia" : "Mendoza",
    "habilidades" : ["C++", "Python"]}

#JSON: un string como un diccionario
json_persona = "{'nombre': 'Ramiro', 'pais': 'Argentina', 'provincia': 'Mendoza', 'habilidades': ['C++', 'Python']}"

#Para cambiar un archivo JSON a diccionario, importamos el modulo json
import json

json_persona = '''{
    "nombre": "Ramiro",
    "pais": "Argentina",
    "provincia": "Mendoza",
    "habilidades": ["C++", "Python"]}'''
diccionario = json.loads(json_persona)
print(type(diccionario))
print(diccionario)

#Archivo CSV
import csv
with open('ejemplo.csv') as f:
    lector_csv = csv.reader(f, delimiter=',')
    contador_lineas = 0
    for fila in lector_csv:
        if contador_lineas == 0:
            print(f'Columnas: {", ".join(fila)}')
            contador_lineas += 1
        else:
            print(f'\t{fila[0]} es programador. El vive en {fila[1]}, {fila[2]}.')
            contador_lineas += 1
    print(f'Numero de lineas: {contador_lineas}')

#Archivo XLSX
#Aqui necesitamos instalar el paquete xlrd
import xlrd
libro = xlrd.open_workbook('ejemplo.xls')
print(libro.nsheets)
print(libro.sheet_names)

#Archivo XML
#Parecido a HTML. Las etiquetas no estan predefinidas. La primera linea es una declaracion
#de XML. La etiqueta 'persona' es la raiz del XML, y tiene un atributo 'genero'.
import xml.etree.ElementTree as ET
arbol = ET.parse('ejemplo.xml')
raiz = arbol.getroot()
print('Etiqueta raiz: ', raiz.tag)
print('Atributo: ', raiz.attrib)
for hijo in raiz:
    print('Campo: ', hijo.tag)

#1. Write a function which count number of lines and number of words in a text.

#All the files are in the data the folder:
#a) Read obama_speech.txt file and count number of lines and words
#b) Read michelle_obama_speech.txt file and count number of lines and words
#c) Read donald_speech.txt file and count number of lines and words
#d) Read melina_trump_speech.txt file and count number of lines and words
with open('data/obama_speech.txt') as f:
    lista = f.read().splitlines()
    print(len(lista))
    import re
    f.seek(0,0)
    string = f.read()
    contador = re.findall(r'\w', string, re.I)
    print(len(contador)) #A

with open('data/michelle_obama_speech.txt') as f:
    lista = f.read().splitlines()
    print(len(lista))
    f.seek(0,0)
    string = f.read()
    contador = re.findall(r'\w', string, re.I)
    print(len(contador)) #B

with open('data/donald_speech.txt') as f:
    lista = f.read().splitlines()
    print(len(lista))
    f.seek(0,0)
    string = f.read()
    contador = re.findall(r'\w', string, re.I)
    print(len(contador)) #C

with open('data/melina_trump_speech.txt') as f:
    lista = f.read().splitlines()
    print(len(lista))
    f.seek(0,0)
    string = f.read()
    contador = re.findall(r'\w', string, re.I)
    print(len(contador)) #D

#2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages.
with open('data/countries_data.json', 'r', encoding='utf-8') as f:
    coso = f.read()
    lista = json.loads(coso)
    print(type(lista))
    idiomas = []
    for diccionario in lista:
        for idioma in diccionario['languages']:
            idiomas.append(idioma)
