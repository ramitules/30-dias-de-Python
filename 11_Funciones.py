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
def calcular_pendiente()