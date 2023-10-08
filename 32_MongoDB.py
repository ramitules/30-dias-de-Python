from pymongo import *

#Lanzar cliente
cliente = MongoClient()

#Instanciar una base de datos
db = cliente.VST

    #Tambien se puede utilizar nomenclatura de diccionario
db = cliente['VST']

#Seleccionar coleccion
escuelas = db.schools

nueva_escuela = {'tenant_id': 1234}

#Insertar documento. Debe ser diccionario (key:value). Retorna un resultado
insert_resultado = escuelas.insert_one(nueva_escuela)
print(insert_resultado.inserted_id)

#Buscar documento. Pasar como argumento algun filtro, 
#de lo contrario devuelve el primer documento de la coleccion
documento: dict = escuelas.find_one({'school':'pomona2'})
#Tambien se puede utilizar .find(), el cual es un cursor para iterar
#en toda la coleccion, con varios resultados posibles

#Contar documentos. Se pueden filtrar
cantidad = escuelas.count_documents({})

#Eliminar documento
delete_resultado = escuelas.delete_one({'tenant_id': 1234})
print(delete_resultado)