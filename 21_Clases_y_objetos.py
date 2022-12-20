# CLASES Y OBJETOS

# Python es en si un lenguaje orientado a objetos. Todo en Python es un objeto, con sus propiedades
# y metodos. Un numero, string, lista, diccionario, tupla, conjunto, etc. utilizado en un
# programa es un objeto de una clase preestablecida. Creamos clases para crear objetos. Una clase
# es como un constructor de objetos. Instanciamos una clase para crear un objeto. La clase define
# atributos y el comportamiento del objeto, mientras que el objeto representa la clase.

# Para crear una clase, utilizamos CLASS ... Generalmente se escribe con primer letra mayuscula.
class Persona:
    pass
print(Persona) # <class '__main__.Persona'>

# Podemos crear un objeto desde la clase
p = Persona()
print(p) # <__main__.Persona object at 0x000001A6DE165D80>

# Una clase sin constructor no es muy util. Siempre debemos crearla con un constructor llamado
# INIT(self, ...)

class Provincia: # Con parametros por defecto, se evitan errores de inicializacion
    def __init__(self, nombre='Buenos Aires', poblacion=15625084, idioma='espannol'):
        self.nombre = nombre
        self.poblacion = poblacion
        self.idioma = idioma
    # Tambien pueden tener metodos (funciones que pertenecen al objeto)
    def mostrar(self):
        return f'{self.nombre}, poblacion: {self.poblacion} habitantes, se habla {self.idioma}'

c = Provincia('Mendoza', 937154, 'espannol')
c2 = Provincia()
print(c)
print(c.mostrar())
print(c2.mostrar())

# HERENCIA
# Utilizando herencia se puede reutilizar codigo. La herencia nos permite definir una clase
# que herede los metodos y propiedades de la clase base.
class ProvinciasMundiales(Provincia):
    # No es necesario, pero podemos annadir un constructor dentro de la clase hija
    # Haciendo esto, sobreescribimos el constructor heredado con SUPER()
    def __init__(self, nombre='Mendoza', poblacion=937154, idioma='espannol', locacion='Oeste'):
        self.locacion = locacion
        super().__init__(nombre, poblacion, idioma)
    def mostrar(self):
        return f'{self.nombre}, poblacion: {self.poblacion} habitantes, se habla {self.idioma} y queda en el {self.locacion}.'

prov1 = ProvinciasMundiales('Salta', 999, 'espannol','Norte')
print(prov1.mostrar())
prov2 = ProvinciasMundiales()
print(prov2.mostrar())