# DICCIONARIOS
"""
Un diccionario es una coleccion de datos desordenados, modificables y emparejados (key: valor).
"""

#Para crear un diccionario se usa {}, o DICT{}

dicc = {}
Persona = {
    'Primer nombre':'Ramiro',
    'Apellido':'Tules',
    'Edad': 25,
    'Provincia':'Mendoza',
    'Estado civil':'Soltero',
    'Habilidades':['HTML','CSS','C++','Python'],
    'Direccion':{
        'Calle':'Corrientes',
        'Codigo Postal':'M5537'}
    } #Los diccionarios pueden contener multiples tipos de datos, desde STRINGS hasta otros diccionarios.

#En este caso, LEN() se utiliza para saber la cantidad de elementos emparejados (key: valor)
print(len(Persona))

#Para acceder a los elementos del diccionario, usamos su KEY
print(Persona['Primer nombre']) #Si no existe el elemento, arroja ERROR

#Para que no arroje error una busqueda, utilizamos .GET()
print(Persona.get('Estado')) #Arroja NONE

