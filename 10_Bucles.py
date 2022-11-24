# BUCLES
"""
La vida esta llena de rutinas. En programacion tambien tenemos muchas tareas repetitivas. Para poder administrar estas tareas en un lenguaje, usamos bucles.
Python posee los bucles WHILE y FOR


# Usamos WHILE para ejecutar un conjunto de tareas hasta que una condicion se cumpla. Cuando la condicion se torna falsa,
# continua la ejecucion despues del bucle.
contar = 0
while contar < 5:
    print(contar)
    contar = contar + 1

# Si queremos ejecutar algo cuando la condicion no se cumpla mas, usamos ELSE
while contar < 5:
    print(contar)
    contar = contar + 1
else: print(contar) #5

# Para detener un bucle, utilizamos BREAK
while contar < 5:
    print(contar)
    contar = contar + 1
    if contar == 3:
        break

# Podemos continuar un bucle con CONTINUE
count = 0
while count < 5:
    if count == 3: continue
    print(count)
    count = count + 1 
    
# Crear bucles con FOR
# Para listas:
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: 
    print(number)

# Para strings:
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# Para tuplas:
numbers = (0, 1, 2, 3, 4, 5)
for i in numbers:
    print(i)

# Para diccionarios:
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # De esta manera obtenemos las keys y los valores

# Para conjuntos:
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# BREAK y CONTINUE se utilizan de la misma manera que en WHILE
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
    
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # Para condiciones Short Hand se necesitan ambos IF y ELSE
print('outside the loop')

# Para listar numeros se utiliza RANGE(comienzo, final, pasos). Por defecto, comienza en 0 y se incrementa de a 1 paso, pero necesita
# al menos un argumento (final).
lista = list(range(11))
print(lista)
conjunto = set(range(1,11)) # Con dos argumentos se setea comienzo y final
print(conjunto)

lista = list(range(0, 11, 2))
print(lista)

for number in range(11): print(number)

# Se pueden anidar FORs
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# Para mostrar algun mensaje al finalizar un bucle, se utiliza ELSE
for number in range(11):
    print(number)
else:
    print('The loop stops at', number)

# In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
# En Python, cuando una declaracion es requerida despues de dos puntos, pero no queremos ejecutar ningun codigo, podemos escribir PASS para evitar errores.
# Tambien lo podemos utilizar como un marcador para futuras declaraciones
for number in range(6):
    pass


#1. Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11): print(number)

cont = 0
while cont < 11:
    print(cont)
    cont = cont + 1
   
#2. Iterate 10 to 0 using for loop, do the same using while loop.
cont = 10
while cont > -1:
    print(cont)
    cont = cont -1
    
for number in range(10, -1, -1): print(number)

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
for number in range(1, 8): print('#' * number)

#4. Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for x in range(1, 9):
    print('# ' * 8)
    
#5. Print the following pattern:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
for x in range(11): print(x, 'x', x, '=', x * x)

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lista = ['Python', 'Numpy','Pandas','Django', 'Flask']
for x in lista: print(x)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
for x in range(100):
    if x % 2 == 0: print(x)
    
#8. Use for loop to iterate from 0 to 100 and print only odd numbers
for x in range(100):
    if x % 2 != 0: print(x)

#9. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
suma = 0
for x in range(101): suma = suma + x
else:
    print(suma)

#10. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
suma_pares = 0
suma_impares = 0
for x in range(101):
    if x % 2 == 0: suma_pares = suma_pares + x
    else: suma_impares = suma_impares + x
else: print('La suma de los pares es: ', suma_pares,'. Y la suma de los impares es: ', suma_impares)

#11. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from countries import countries as count
for x in count:
    if 'land' in x: print(x)
    #12. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
frutas = ['banana', 'orange', 'mango', 'lemon']
aux = str()
for x in range(1, 3):
    aux = frutas[x - 1]
    frutas[x - 1] = frutas[-x]
    frutas[-x] = aux
else: print(frutas)
"""
#13. Go to the data folder and use the countries_data.py file. 
from countries_data import paises as p

#What are the total number of languages in the data
idiomas = set()

for x in p:
    idiomas.update(x.get('languages'))
else: print(len(idiomas))

#Find the ten most spoken languages from the data

#Find the 10 most populated countries in the world
mas_poblados = []

for x in p:
    mas_poblados.append(x.get('population'))
else: mas_poblados.sort(reverse = True)

for x in range(11):
    print(mas_poblados[x])
