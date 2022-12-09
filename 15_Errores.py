#ERRORES EN PYTHON

#Cuando escribimos codigo, es comun que cometamos errores de tipeo o de otros tipos. Si nuestro codigo falla al correr, el interprete
#arrojara un mensaje, conteniendo informacion acerca de donde se origino el problema y el tipo de error.
#A veces tambien nos dara consejos de como arregarlo. Entender los diferentes tipos de errores en lenguajes de programacion nos ayudara a
#eliminar bugs en nuestro codigo de forma rapida, ademas de mejorar en lo que hacemos.

#veamos los errores mas comunes uno por uno con shell interactivo de Python.

#Error de sintaxis (SyntaxError):
#print 'hello world'
#  File "<stdin>", line 1
#    print 'hello world'
#                      ^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?

#Error de nombre (NameError):
#print(age)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'age' is not defined

#Error de indice (IndexError):
#numbers = [1, 2, 3, 4, 5]
#numbers[5]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#IndexError: list index out of range

#Modulo no encontrado (ModuleNotFoundError):
#import maths <--
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ModuleNotFoundError: No module named 'maths'

#Error de atributo (AttributeError):
#import math
#math.PI
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: module 'math' has no attribute 'PI'

#Error de key (KeyError):
#users = {'name':'Asab', 'age':250, 'country':'Finland'}
#users['name']
#'Asab'
#users['county']
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'county'

#Error de tipo (TypeError):
#4 + '3'
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: unsupported operand type(s) for +: 'int' and 'str'