# CONJUNTOS
"""
Conjunto es una coleccion de elementos desordenados, distintos y sin indice.
En Python un conjunto es usado para almacenar elementos unicos, y es posible hallar la union, interseccion, diferencia, diferencia simetrica, subconjunto, superconjunto y conjunto disjunto entre conjuntos.
"""

#Creacion de un conjunto vacio

st = {}

frutas = {'Banana', 'Naranja', 'Pera', 'Uva'}

#Chequear que exista un item
'Banana' in frutas

#Annadir items con .ADD()
frutas.add('Manzana')

#Annadir multiples items con .UPDATE(items), toma una lista de argumentos
frutas.update(['Kiwi', 'Anana', 'Melon'])

#Eliminar items con .REMOVE(), si no lo encuentra, arroja error
frutas.remove('Manzana')

#Remover un item aleatorio con .POP()
frutas.pop()

#Limpiar un conjunto con .CLEAR()
frutas.clear()

#Eliminar un conjunto con DEL
del frutas

#Se pueden convertir listas a conjuntos. Convertir una lista a conjunto elimina duplicados y desordena los elementos
verduras = ['Lechuga', 'Tomate', 'Palta', 'Limon', 'Lechuga']
set_verduras = set(verduras)

#Para unir dos conjuntos se utiliza .UNION(conjunto)
set_frutas = {'Manzana', 'Naranja', 'Mandarina'}
print(set_verduras.union(set_frutas))

#INTERSECTION devuelve los elementos que estan en ambos conjuntos
todos = {1, 2, 3, 4, 5, 6}
pares = {2, 4, 6, 8, 10}
interseccion = todos.intersection(pares)
print(interseccion)

#Para saber si un conjunto es subconjunto o superconjunto de otro, se utiliza .ISSUBSET() y .ISSUPERSET()
print(pares.issubset(todos))

#Para saber la diferencia entre dos conjuntos, se utiliza .DIFFERENCE()
print(todos.difference(pares)) #1, 3, 5

#.SYMMETRIC_DIFERENCE(conjunto) devuelve la diferencia simetrica entre dos conjuntos.
# Significa que devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los que estan presentes en ambos a la vez
print(todos.symmetric_difference(pares))

#Si dos conjuntos no tienen elementos en comun, son conjuntos disjuntos. Se puede chequear con .ISDISJOINT(conjunto)
print(todos.isdisjoint(pares))

#1. Find the length of the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Ramiro', 'Tules'])

#4. Remove one of the companies from the set it_companies
it_companies.pop()

#5. What is the difference between remove and discard
# DISCARD no arroja error al no encontrar un elemento, REMOVE si.

#6. Join A and B
join_AB = A.union(B)

#7. Find A intersection B
intersection_AB = A.intersection(B)

#8. Is A subset of B
print(A.issubset(B))

#9. Are A and B disjoint sets
print(A.isdisjoint(B))

#10. Join A with B and B with A
A = A.union(B)
B = B.union(A)

#11. What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#12. Delete the sets completely
del A, B, it_companies

#13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
print(len(ages_set), len(age))

#14. Explain the difference between the following data types: string, list, tuple and set
# STRING es una cadena de caracteres. LIST es un conjunto de datos ordenados y modificables. TUPLE es un conjunto de datos
# ordenados y no modificables. SET es un conjunto de datos no ordenados ni modificables, sin duplicados.

#15. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
string = 'I am a teacher and I love to inspire and teach people'

lista = string.split()
list_set = set(lista)
print(len(list_set), list_set)