# FUNCIONES
"""
Hasta ahora vimos varias funciones preestablecidas de Python. En esta seccion, vamos a centrarnos en funciones propias.
Que es una funcion? Antes de arrancar, definamos lo que es y por que las necesitamos.
Una funcion es un bloque de codigo disenado para ejecutar cierta tarea. Para definir o declarar una funcion, utilizamos DEF.
El bloque de codigo de la funcion solo es ejecutado si la funcion es llamada.

# Las funciones pueden crearse sin parametros
def generar_nombre_completo():
	primer_nombre = 'Ramiro'
	segundo_nombre = 'Gaston'
	apellido = 'Tules'
	espacio = ' '
	nombre_completo = primer_nombre + espacio + segundo_nombre + espacio + apellido
	print(nombre_completo)

generar_nombre_completo()

# Ademas, pueden devolver un valor con RETURN. Si no se especifica un valor de retorno, devuelve NONE
def anadir_dos_numeros():
	a = 1
	b = 5
	c = a + b
	return c

print(anadir_dos_numeros())

# Funciones con parametros
def bienvenida(nombre):
	mensaje = nombre + ', bienvenido a mi programa!'
	return mensaje

print(bienvenida('Ramiro'))

def calcular_edad(anio, anio_nacimiento):
	edad = anio - anio_nacimiento
	return edad

print('Tu edad es: ', calcular_edad(2022, 1997))

# Si enviamos como parametros los key y sus valores, no tenemos que preocuparnos por el orden
def anadir_numeros(num1, num2, num3):
	total = num1 + num2 + num3
	return total
print(anadir_numeros(num3 = 3, num1 = 2, num2 = 100))

# A veces pasamos valores por defecto como parametros. Si no se envian parametros, se utilizan los que haya por defecto
def peso_de_objeto(masa, gravedad = 9.81):
	peso = str(masa * gravedad) + ' N'
	return peso

print('Peso del objeto expresado en Newtons: ', peso_de_objeto(200))

# Si no sabemos la cantidad de argumentos que se le pasa a una funcion, se crea una cantidad arbitraria de argumentos
# con * antes del nombre del parametro
def suma_total(*numeros):
	total = 0
	for numero in numeros: total += numero
	return total

print(suma_total(1, 3, 6, 19, 20))

# Ejemplo con parametro por defecto y numero arbitrario de parametros
def generar_grupos(grupo, *nombres):
	print(grupo)
	for x in nombres: print(x)

print(generar_grupos('Python', 'El', 'Ella', 'Ellos'))
"""
#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
from mailbox import NoSuchMailboxError
from tkinter.ttk import setup_master


def anadir_dos_numeros(num1, num2):
	suma = num1 + num2
	return suma

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_circulo(radio):
	pi = 3.14
	area = pi * radio * radio
	return area

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def anadir_numeros(*numeros):
	suma = 0
	for n in numeros:
		if type(n) == int: suma += n
		else:
			print('No es un numero')
			continue
	else: return suma

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convertir_celsius_a_fahrenheit(celsius):
	f = (celsius * 9 / 5) + 32
	return f

#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def chequear_temporada(mes):
	verano = ['Diciembre', 'Enero', 'Febrero']
	otonio = ['Marzo', 'Abril', 'Mayo']
	invierno = ['Junio', 'Julio', 'Agosto']
	primavera = ['Septiembre', 'Octubre', 'Noviembre']
	if mes in verano: return 'Verano'
	elif mes in otonio: return 'Otonio'
	elif mes in invierno: return 'Invierno'
	else: return 'Primavera'

#6. Write a function called calculate_slope which return the slope of a linear equation
def calcular_pendiente(y, x, independiente):
	return x

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solucionar_ecuacion_cuadratica(a, b, c):
	x = (-b + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
	x2 = (-b - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)

	solucion = {x, x2}
	return solucion

#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def mostrar_lista(lista):
	for x in lista: print(x)

#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def lista_inversa(*z):
	for x in range(1, len(z)+1): print(z[-x])
	else: return 'Fin'

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def lista_mayusculas(lista):
	mayusculas = []
	for x in lista: mayusculas.append(x.capitalize())
	return mayusculas

frutas = ['banana', 'manzana', 'pera']

#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def anadir_item(lista, item):
	lista2 = []
	for x in lista: lista2.append(x)
	else: lista2.append(item)
	return lista2
	
#12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remover_item(lista, item):
	lista2 = lista.copy()
	lista2.remove(item)
	return lista2

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def suma_de_numeros(numero):
	suma = numero
	for x in range(0, numero): suma += x
	return suma

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def suma_de_pares(numero):
	suma = 0
	if numero % 2 == 0: suma = numero
	for x in range(0, numero):
		if x % 2 == 0: suma += x
	return suma

#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def suma_de_impares(numero):
	suma = 0
	if numero % 2 != 0: suma = numero
	for x in range(0, numero):
		if x % 2 != 0: suma += x
	return suma

#16. Declare a function named evens_and_odds.
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
def pares_e_impares(numero):
	pares = 0
	impares = 0
	for x in range(0, numero):
		if x % 2 == 0: pares += 1
		else: impares += 1
	print('Pares: ', pares)
	print('Impares: ', impares)

#17. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(numero):
	f = 1
	for x in range(1, numero+1): f *= x
	return f

#18. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def vacio(x):
	for y in x: return 'No vacio'
	else: return 'Vacio'

#19. Write a function called is_prime, which checks if a number is prime.
def es_primo(numero):
	if numero > 1:
		aux = 0
		for x in range(1, numero +1):
			if numero % x == 0: aux += 1
		if aux == 2: print('Es primo')
		else: print('No es primo')
	else: print('No es primo')

#20. Write a functions which checks if all items are unique in the list.
def chequear_unicos(lista):
	s = set(lista)
	if len(s) == len(lista): return True
	else: return False

#21. Write a function which checks if all the items of the list are of the same data type.
def chequear_tipo(lista):
	check = lista[0]
	for x in lista:
		if type(x) != type(check): return False
	else: return True