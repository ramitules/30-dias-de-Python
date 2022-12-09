# FUNCIONES DE ORDEN SUPERIOR
"""
En Python, las funciones son tratadas como ciudadanos de primera clase, permitiendonos ejecutar las siguientes acciones:
    Una funcion puede tomar una o mas funciones como parametros
    Una funcion puede devolver otra funcion
    Una funcion puede ser modificada
    Una funcion puede ser asignada a una variable
"""

# Funcion como parametro:
def sumar_numeros(numeros):
    return sum(numeros)

def funcion_alto_nivel(funcion, lista): #Funcion como parametro
    summ = funcion(lista)
    return summ

resultado = funcion_alto_nivel(sumar_numeros, [1, 2, 3, 4, 5])
print(resultado) #15

# Funcion como valor de retorno
def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

def absoluto(x):
    if x >= 0: return x
    else: return -(x)

def funcion_alto_nivel2(tipo): #Funcion retornando otra funcion
    if tipo == 'cuadrado': return cuadrado
    elif tipo == 'cubo': return cubo
    elif tipo == 'absoluto': return absoluto

resultado = funcion_alto_nivel2('cubo')
print(resultado(3)) #27
resultado = funcion_alto_nivel2('absoluto')
print(resultado(-65)) #65

# Cierres de Python
# Python permite que una funcion anidada acceda al scope de la funcion que la envuelve. Esto se conoce como Closure.
# Se crean anidando funciones dentro de otra funcion y retornando la funcion interna:
def anadir_diez():
    diez = 10
    def add(num):
        return num + diez
    return add

closure_result = anadir_diez()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# Decoradores de Python
# Un decorador es un patron de diseno en Python que permite al usuario anadir una nueva funcionalidad a un objeto existente
# sin modificar su estructura. Generalmente son llamadas antes de la definicion de la funcion que queremos decorar.
def bienvenida():
    return 'Bienvenido a Python'

def decorador_mayusculas(funcion):
    def wrapper():
        func = funcion()
        mayusculas = func.upper()
        return mayusculas
    return wrapper

g = decorador_mayusculas(bienvenida)
print(g())

#AHORA IMPLEMENTANDOLO CON UN DECORADOR
def decorador_mayusculas(funcion):
    def wrapper():
        func = funcion()
        mayusculas = func.upper()
        return mayusculas
    return wrapper

@decorador_mayusculas
def bienvenida():
    return 'Bienvenido a Python'

print(bienvenida()) #BIENVENIDO A PYTHON

# Aplicar multiples decoradores a una funcion
# Primer decorador:
def decorador_mayusculas(funcion):
    def wrapper():
        func = funcion()
        mayusculas = func.upper()
        return mayusculas
    return wrapper

#Segundo decorador:
def decorador_divisor_string(funcion):
    def wrapper():
        func = funcion()
        string_dividido = func.split()
        return string_dividido
    return wrapper

@decorador_divisor_string
@decorador_mayusculas #El orden es importante, ya que .upper() no funciona en listas
def bienvenida():
    return 'Bienvenido a Python'
print(bienvenida()) #['BIENVENIDO', 'A', 'PYTHON']

# La mayor parte del tiempo vamos a necesitar que nuestras funciones tomen parametros, por ende necesitamos
# definir un decorador que acepte parametros
def decorador_con_parametros(funcion):
    def wrapper_con_parametros(p1, p2, p3):
        funcion(p1, p2, p3)
        print("Yo vivo en {}".format(p3))
    return wrapper_con_parametros

@decorador_con_parametros
def mostrar_nombre_completo(primer_nombre, apellido, pais):
    print('Me llamo {} {}. Me encanta programar.'.format(primer_nombre, apellido, pais))

mostrar_nombre_completo("Ramiro", "Tules", 'Argentina')

# Funciones de orden superior preestablecidas
# Algunas funciones de orden superior son MAP(), FILTER() y REDUCE(). Una funcion Lambda puede pasarse como
# parametro, es uno de los mejores casos de implementacion de funciones Lambda

# Funcion MAP(funcion, iterable), recorre una lista, devuelve una lista:
numeros = [1, 2, 3, 4, 5] #Lista (iterable)
def cuadrado(x):
    return x ** 2

numeros_al_cuadrado = map(cuadrado, numeros)
print(list(numeros_al_cuadrado))

# Con Lambda:
print(list(map(lambda x: x ** 2, numeros)))

numeros_str = ['1', '2', '3', '4', '5'] #Lista (iterable)
numeros_int = map(int, numeros_str)
print(list(numeros_int))

# Otro ejemplo:
nombres = ['Ramiro', 'Gaston', 'Tules'] #Lista (iterable)
def cambiar_a_mayusculas(nombre):
    return nombre.upper()

nombres_en_mayusculas = list(map(cambiar_a_mayusculas, nombres))
print(nombres_en_mayusculas)

#Con Lambda:
nombres_en_mayusculas = list(map(lambda nombre: nombre.upper(), nombres))
print(nombres_en_mayusculas) #Mismo resultado

# La funcion FILTER(funcion, iterable) retorna un booleano llamando a la funcion y utilizando cada item
# de la lista iterable. Filtra los items que cumplan la condicion. Devuelve una lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

def es_par(numero):
    if numero % 2 == 0: return True
    return False

numeros_pares = list(filter(es_par, numeros))
print(numeros_pares)

# La funcion REDUCE(funcion, iterable) se encuentra en el modulo FUNCTOOLS, por ende hay que importarlo.
# Retorna un solo valor, no retorna listas ni iterables.
from functools import reduce

numeros_str = ['1', '2', '3', '4', '5']

def anadir_dos_numeros(x, y):
    return int(x) + int(y)

total = reduce(anadir_dos_numeros, numeros_str)
print(total)

#1. Explain the difference between map, filter, and reduce.
#MAP() sirve para aplicar una funcion a todos los items en un iterable, teniendo como resultado otra lista
#FILTER() sirve para filtrar una lista segun una condicion, devolviendo una lista
#REDUCE() retorna solo un valor, el resultado de la funcion que se le da como parametro

#2. Explain the difference between higher order function, closure and decorator.
# Una funcion de orden superior puede ser una funcion retornando otra, o una funcion como parametro de otra.
# Closure refiere a una funcion anidada dentro de otra
# Decorator refiere a una funcion que decora a un objeto o a otra funcion

#3. Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for x in countries: print(x)

#4. Use for to print each name in the names list.
names = ['Ramiro', 'Gaston', 'Tules', 'Marchesi']
for x in names: print (x)

#5. Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in numbers: print(x)

#6. Use map to create a new list by changing each country to uppercase in the countries list
nuevo = list(map(lambda x: x.upper(), countries))
print(nuevo)

#7. Use map to create a new list by changing each number to its square in the numbers list
nuevo = list(map(lambda x: x ** 2, numbers))
print(nuevo)

#8. Use map to change each name to uppercase in the names list
nuevo = list(map(lambda x: x.upper(), names))
print(nuevo)

#9. Use filter to filter out countries containing 'land'.
nuevo = list(filter(lambda x: 'land' in x, countries))
print(nuevo)

#10. Use filter to filter out countries having exactly six characters.
nuevo = list(filter(lambda x: len(x) == 6, countries))
print(nuevo)

#11. Use filter to filter out countries containing six letters and more in the country list.
print(list(filter(lambda x: len(x) >= 6, countries)))

#12. Use filter to filter out countries starting with an 'E'
print(list(filter(lambda x: x[0] == 'E', countries)))

#13. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def listaString(l):
    string = [str(i) for i in l]
    return string

print(listaString(numbers))

