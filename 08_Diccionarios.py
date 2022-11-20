# DICCIONARIOS
"""
Un diccionario es una coleccion de datos desordenados, modificables y emparejados (key: valor).
"""
#Para crear un diccionario se usa {}, o DICT{}

dicc = {}
Persona = {
    'Primer_nombre':'Ramiro',
    'Apellido':'Tules',
    'Edad': 25,
    'Provincia':'Mendoza',
    'Estado_civil':'Soltero',
    'Habilidades':['HTML','CSS','C++','Python'],
    'Direccion':{
        'Calle':'Corrientes',
        'Codigo_Postal':'M5537'}
    } #Los diccionarios pueden contener multiples tipos de datos, desde STRINGS hasta otros diccionarios.

#En este caso, LEN() se utiliza para saber la cantidad de elementos emparejados (key: valor)
print(len(Persona))

#Para acceder a los elementos del diccionario, usamos su KEY
print(Persona['Primer_nombre']) #Si no existe el elemento, arroja ERROR

#Para que no arroje error una busqueda, utilizamos .GET()
print(Persona.get('Estado')) #Arroja NONE

#Se annaden keys y elementos de la siguiente manera
Persona['Job_Title'] = 'Programador'
Persona['Habilidades'].append('SQL')

#Podemos modificar elementos en un diccionario con su key
Persona['Primer_nombre'] = 'Gaston'

#Para buscar una key, se utiliza IN
print('Provincia' in Persona) #True

#Se utiliza POP(key) para remover un item con una key especificada, POPITEM() para remover el ultimo item, y DEL
Persona.pop('Edad')
Persona.popitem() #Remueve el item 'Job_Title'
del Persona['Estado_civil']

#.ITEMS() cambia el diccionario a una lista de tuplas
print(Persona.items())

#Para limpiar un diccionario se utiliza .CLEAR()
Persona.clear()

#Para eliminar completamente un diccionario, se utiliza DEL
del Persona

#Podemos copiar un diccionario con .COPY(). Utilizando este metodo, se evita la modificacion/mutacion del diccionario original
dct = {'key1':'rgb'}
dct_copia = dct.copy()

#Para obtener todas las keys de un diccionario como una lista, se utiliza .KEYS()
print(dct.keys())

#Para obtener todos los valores de un diccionario como una lista, se utiliza .VALUES()
print(dct.values())

#1. Create an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    'Nombre': 'Pichicho',
    'Color':'Blanco',
    'Raza':'Caniche feo',
    'Patas':'Marrones',
    'Edad':3}

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Estudiante = {
    'Primer_nombre': 'Ramiro',
    'Apellido': 'Tules',
    'Sexo': 'Si',
    'Edad': 25,
    'Estado_civil': 'Soltero',
    'Habilidades':['HTML','CSS','C++','Python'],
    'Provincia':'Mendoza',
    'Ciudad': 'Las_Heras',
    'Direccion': 'Corrientes'}

#4. Get the length of the student dictionary
print(len(Estudiante))

#5. Get the value of skills and check the data type, it should be a list
print(Estudiante.get('Habilidades'), type(Estudiante['Habilidades']))

#6. Modify the skills values by adding one or two skills
Estudiante['Habilidades'].append('SQL')

#7. Get the dictionary keys as a list
lista = Estudiante.keys()

#8. Get the dictionary values as a list
valores = Estudiante.values()

#9. Change the dictionary to a list of tuples using items() method
Estudiante = Estudiante.items()

#10. Delete one of the items in the dictionary
dog.pop('Nombre')
print(dog)

#11. Delete one of the dictionaries
del dog