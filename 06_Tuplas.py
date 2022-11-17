#	TUPLAS
"""
Una tupla es una coleccion de diferentes tipos de datos, los cuales estan ordenados y no son modificables. Son escritas con ().
Cuando una tupla es creada, no podemos modificar sus valores (no se puede utilizar ADD, INSERT, REMOVE).
Tienen ciertos metodos relacionados a las tuplas:
	TUPLE()
	COUNT()
	INDEX()
"""

tupla_vacia = () 
tupla_vacia_2 = tuple()

frutas = ('Banana', 'Manzana', 'Pera', 'Mango')

print(len(frutas)) # 4

#Acceder a items
primer_fruta = frutas[0]
ultima_fruta = frutas[-1]

#Cambiar de tupla a lista
frutas = list(frutas)

#Cambiar de lista a tupla
frutas = tuple(frutas)

#Chequear que un item este en la tupla con IN
print('Banana' in frutas) # True

#Eliminar tuplas
del frutas

#1. Crear una tupla vacia

tupla = ()

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('Banana', 'Manzana')
vegetables = ('Cebolla', 'Lechuga')
animal = ('Atun', 'Churrasco')
food_stuff_tp = fruits + vegetables + animal

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

mitad = food_stuff_tp[int(len(food_stuff_tp)/2)]

#5. Slice out the first three items and the last three items from food_staff_lt list

primera_mitad = food_stuff_lt[0:3]
segunda_mitad = food_stuff_lt[-4:-1]

#6. Delete the food_staff_tp tuple completely

del food_stuff_tp

#7. Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)