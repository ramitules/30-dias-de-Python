#VARIABLES
print (type(print ("caca")))    #nonetype
print (type(1))                 #int
print (type("caca"))            #str
print (type(1.5))               #float
print (type(False))             #bool
print (type(3 + 1j))            #complex

#INPUTS
age = input("Cual es tu edad? ")
name = input("Cual es tu nombre? ")
print (name, age)

#CAMBIO DE TIPO
name = 25
age = "Ramiro Tules"
print (name, age)
print (type(name))

#FORZAR EL TIPO
adress: str = "Mi direccion"
adress = "12 de Octubre 10541"
print (adress)
adress = False
print (type(adress)) #NO SE PUEDE FORZAR EL TIPO :)