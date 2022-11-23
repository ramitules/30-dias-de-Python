# CONDICIONALES
"""
Por defecto, las declaraciones en Python son ejecutadas secuencialmente de arriba hacia abajo. 
Si el procesamiento logico lo requiere, el flujo de secuencias de la ejecucion pueden alterarse de dos maneras:
    -> Ejecucion condicional: un bloque de una o mas declaraciones seran ejecutadas si una cierta expresion es verdadera.
    -> Ejecucion repetitiva: un bloque de una o mas declaraciones seran repetitivamente ejecutadas mientras una cierta expresion sea verdadera.

En esta seccion, veremos las declaraciones IF, ELSE, ELIF. Los operadores logicos y de comparacion que vimos en secciones anteriores seran de utilidad aqui.


a = 3

if a>0:
    print('Es positivo')
else:
    print('Es negativo')

#Se utiliza ELIF para agregar mas de una condicion IF
b = 0
if b>0:
    print('Es positivo')
elif b<0:
    print('Es negativo')
else:
    print('Es cero')

#Short Hand
print('"a" es positivo') if a>0 else print('"a" es negativo')

#Condiciones anidadas
a = 0
if a>0:
    if a%2==0: print('A es un numero positivo y par')
    else: print('A es un numero positivo')
elif a==0: print('A es cero')
else: print('A es un numero negativo')

#Utilizando AND para no anidar condiciones
if a > 0 and a % 2 == 0: print('A es un numero positivo y par')
elif a > 0 and a % 2 != 0: print('A es un numero positivo')
elif a == 0: print ('A es cero')
else: print('A es negativo')

#Utilizando OR
user = 'Ramiro'
access_level = 3
if user == 'admin' or access_level >=4: print('Acceso concedido')
else: print('Acceso denegado')

#1. Get user input using input("Enter your age: "). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years.
edad = int(input('Introduzca su edad: '))
if edad >= 18: print('Puede conducir')
else: print('No puede conducir')

#2. Compare the values of my_age and your_age using if ... else. Who is older (me or you)? Use input(Enter your age: ) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
tu_edad = 20
if edad == tu_edad: print('Tenemos la misma edad')
elif abs(edad-tu_edad) == 1:
    if edad > tu_edad: print('Te llevo un anio')
    else: print('Me llevas un anio')
else:
    if edad > tu_edad: print('Te llevo ',abs(edad-tu_edad))
    else: print('Me llevas ',abs(edad-tu_edad))

#3. Get two numbers from the user using input prompt.
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = int(input('Primer numero: '))
b = int(input('Segundo numero: '))
if a > b: print('"a" es mayor que "b"')
elif a < b: print ('"a" es menor que "b"')
else: print('Son iguales')

#4. Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
puntos = int(input())
calificacion = 'x'
if puntos >= 80: calificacion = 'A'
elif puntos >=70: calificacion = 'B'
elif puntos >=60: calificacion = 'C'
elif puntos >=50: calificacion = 'D'
else: calificacion = 'F'
print(calificacion)

#5. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter. March, April or May, the season is Spring. June, July or August, the season is Summer.
mes = input()
verano = ['Diciembre', 'Enero', 'Febrero']
otonio = ['Marzo', 'Abril', 'Mayo']
invierno = ['Junio', 'Julio', 'Agosto']
primavera = ['Septiembre', 'Octubre', 'Noviembre']
if mes in verano: print('Verano')
elif mes in otonio: print('Otonio')
elif mes in invierno: print('Invierno')
else: print('Primavera')

#6. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
#  If the fruit exists print('That fruit already exist in the list')
fruta = str(input())
if fruta in fruits: print('La fruta ya existe en la lista')
else:
    fruits.append(fruta)
    print(fruits)
"""
#7. Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Ramiro',
    'last_name': 'Tules',
    'age': 25,
    'country': 'Argentina',
    'is_marred': False,
    'skills': ['HTML', 'CSS', 'C++', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#  Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person: print(person['skills'][int(len(person['skills'])/2)])

#  Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person: print('Python' in person['skills'])

#  If a person skills has only JavaScript and React, print('He is a front end developer'),
if ['Javascript', 'React'] in person['skills']: print('Es un desarrollador front end') 

#  if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB,
#  Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if ['Python', 'MongoDB'] in person['skills']: print('Es un desarrollador back end')
elif ['React', 'Node', 'MongoDB'] in person['skills']: print('Es un desarrollador full stack')
else: print('Titulo desconocido')

#  If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] == True and 'Finland' in person['country']: print('Asabeneh Yetayeh lives in Finland. He is married.')