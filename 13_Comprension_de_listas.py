# LISTAS DE COMPRENSION
"""
Comprension de listas en Python es una forma compacta de crear una lista desde una secuencia.
Es considerablemente mas rapido que procesar una lista usando el bucle FOR.
"""

# Por ejemplo, si quisieramos cambiar un string a una lista de caracteres
lenguaje = 'Python'
lista = list(lenguaje) #Cambiando el string a una lista
print(lista)

lista = [i for i in lenguaje] #A traves de comprension de listas
print(lista)

# Si quisieramos generar una lista de numeros
numeros = [i for i in range(11)] #Del 0 al 10
print(numeros)

cuadrados = [i * i for i in range(11)] #Se pueden ejecutar operaciones matematicas dentro
print(cuadrados)

numeros = [(i, i * i) for i in range(11)] #Es posible crear una lista de tuplas
print(numeros)

# Tambien pueden combinarse con condicionales
numeros_pares = [i for i in range(21) if i % 2 == 0]
print(numeros_pares)

lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_plana = [numero for fila in lista_de_listas for numero in fila] #Aplanar vector de tres dimensiones
print(lista_plana)

# Las funciones LAMBDA son pequenas funciones sin nombre. Pueden tomar cualquier cantidad de argumentos, pero solo pueden tener una expresion.
# Las necesitamos cuando queremos crear una funcion anonima dentro de otra funcion.
# Para crear una funcion LAMBDA utilizamos LAMBDA + parametros: expresion. No utiliza un retorno pero explicitamente retorna la expresion.
anadir_dos_numeros = lambda a, b: a + b
print(anadir_dos_numeros(2, 3))

print((lambda a, b: a + b)(2, 3)) #Funcion lambda que se autoinvoca

cubo = lambda x: x ** 3
print(cubo(3))

# Usar una funcion LAMBDA dentro de otra funcion
def potencia(x):
    return lambda n: x ** n

cubo = potencia(2)(3) # La funcion "potencia" ahora necesita dos argumentos en parentesis separados
print(cubo)

#1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lista1 = [i for i in numbers if i <= 0]
print(lista1)

#2. Flatten the following list of lists of lists to a one dimensional list:
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
listaaux = [i for x in list_of_lists for i in x]
lista2 = [i for x in listaaux for i in x]
print(lista2)

#3. Using list comprehension create the following list of tuples:
#[(0, 1, 0, 0, 0, 0, 0),
#(1, 1, 1, 1, 1, 1, 1),
#(2, 1, 2, 4, 8, 16, 32),
#(3, 1, 3, 9, 27, 81, 243),
#(4, 1, 4, 16, 64, 256, 1024),
#(5, 1, 5, 25, 125, 625, 3125),
#(6, 1, 6, 36, 216, 1296, 7776),
#(7, 1, 7, 49, 343, 2401, 16807),
#(8, 1, 8, 64, 512, 4096, 32768),
#(9, 1, 9, 81, 729, 6561, 59049),
#(10, 1, 10, 100, 1000, 10000, 100000)]
lista3 = [(i, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5, i ** 6) for i in range(11)]

#4. Flatten the following list to a new list

#5. Change the following list to a list of dictionaries:
