# MANIPULAR EXCEPCIONES

#Python utiliza TRY y EXCEPT para manejar errores. Una salida elegante (o manipulacion elegante) de errores es un codigo
#simple - un programa detecta un error serio y sale "elegantemente", de una forma controlada. Usualmente el programa arroja
#un error descriptivo al terminal o registro, esto hace nuestra aplicacion mas robusta. Generalmente la causa de una excepcion
#es externa al programa en si. Un ejemplo de una excepcion puede ser un input incorrecto, nombre de archivo incorrecto, 
#no se encuentra el archivo, mal funcionamiento de un dispositivo E/S. Las salidas elegantes previenen errores.

#Si usamos TRY y EXCEPT, no arrojaremos errores en los bloques
#try:
#    print(10 + '5')
#except:
#    print('Algo salio mal')

#try:
#    nombre = input('Introduci tu nombre: ')
#    anio_nacimiento = input('Anio de nacimiento: ')
#    edad = 2022 - anio_nacimiento
#    print(f'Sos {nombre}. Y tu edad es {edad}.')
#except TypeError:
#    print('Type error occured')
#except ValueError:
#    print('Value error occured')
#except ZeroDivisionError:
#    print('zero division error occured')

#try:
#    nombre = input('Introduci tu nombre: ')
#    anio_nacimiento = input('Anio de nacimiento: ')
#    edad = 2022 - int(anio_nacimiento)
#    print(f'Sos {nombre}. Y tu edad es {edad}.')
#except TypeError:
#    print('Type error occured')
#except ValueError:
#    print('Value error occured')
#except ZeroDivisionError:
#    print('zero division error occured')
#else:
#    print("Generalmente me ejecuto con el bloque TRY")
#finally:
#    print("Siempre me ejecuto")

#try:
#    nombre = input('Introduci tu nombre: ')
#    anio_nacimiento = input('Anio de nacimiento: ')
#    edad = 2022 - int(anio_nacimiento)
#    print(f'Sos {nombre}. Y tu edad es {edad}.')
#except Exception as e:
#    print(e)

#Empaquetar y desempaquetar argumentos en Python
#Utilizamos dos operadores:
# * para tuplas
# ** para diccionarios

#Desempaquetado de listas
from ast import DictComp


def suma_de_cinco_numeros(a, b, c, d, e):
    return a + b + c + d + e

lista = [1, 2, 3, 4, 5]
print(suma_de_cinco_numeros(*lista)) #Si pasamos la lista sin * arroja error, ya que pide enteros, no iterables

numeros = range(2, 7)
print(list(numeros)) #[2, 3, 4, 5, 6]

argumentos = [2, 7]
numeros2 = range(*argumentos) #Toma argumentos desempaquetados de una lista
print(list(numeros2)) #Igual

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)

numeros = [1, 2, 3, 4, 5, 6, 7]
primero, *medio, ultimo = numeros
print(primero, medio, ultimo) # 1 [2, 3, 4, 5, 6] 7

#Desempaquetado de diccionarios
def desempaquetar_info_persona(nombre, pais, ciudad, edad):
    return f'{nombre} vive en {ciudad}, {pais}. Tiene {edad} anios.'

diccionario = {
    'nombre' : 'Ramiro',
    'pais' : 'Argentina',
    'ciudad': 'Mendoza',
    'edad' : 25}

print(desempaquetar_info_persona(**diccionario))

#EMPAQUETADO
#A veces no sabemos la cantidad de argumentos que una funcion necesita. Podemos utilizar el metodo
#de empaquetado para que la funcion pueda tomar una cantidad ilimitada de argumentos

#Empaquetado de listas
def sumar_todo(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sumar_todo(1, 2, 3, 4, 5, 6, 7, 8, 9)) #45

#Empaquetado de diccionarios
def empaquetar_info_persona(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(empaquetar_info_persona(nombre = 'Ramiro', pais = 'Argentina', ciudad = 'Mendoza', edad = 25))

#SPREADING (extension)
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista = [0, *lista1, *lista2]
print(lista) #[0, 1, 2, 3, 4, 5, 6]

#ENUMERAR - si queremos obtener el indice de una lista
for index, item, in enumerate([20, 30, 40]):
    print(index, item)

paises = ['Argentina', 'Venezuela', 'Chile']
for index, i in enumerate(paises):
    if i == 'Argentina':
        print(f'El pais {i} fue encontrado en el indice {index}')

#ZIP - Si queremos combinar listas mientras iteramos entre ellas
frutas = ['banana', 'manzana', 'pera']
verduras = ['acelga', 'choclo', 'cebolla']
frutas_y_verduras = []
for f, v in zip(frutas, verduras):
    frutas_y_verduras.append({'Fruta':f, 'Verdura':v})

print(frutas_y_verduras)