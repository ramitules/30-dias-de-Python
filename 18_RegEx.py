# EXPRESIONES REGULARES

#Una expresion regular o RegEx es una cadena de texto especial que permite encontrar patrones en datos.
#Una RegEx puede ser usada para saber si existe un patron en un tipo de datos diferente.
#Para utilizar RegEx debemos importar el modulo RE

import re

#Metodos en el modulo RE
#Para encontrar un patron utilizamos diferentes conjuntos de caracteres RE
#   re.match(): busca solo en la primera linea del string y retorna coincidencias si las encuentra, sino retorna None.
#   re.search(): retorna una coincidencia si hay alguna en algun lugar del string, incluyendo strings de varias lineas.
#   re.findall(): retorna una lista con todas las coincidencias.
#   re.split(): toma un string, lo divide en las coincidencias, y devuelve una lista.
#   re.sub(): reemplaza una o varias coincidencias en un string.

#Match
txt = "Me encanta programar en Python"
match = re.match('Me encanta programar', txt, re.I) #re.I para ignorar mayusculas
print(match) #<re.Match object; span=(0, 20), match='Me encanta programar'>

span = match.span() #Obtenemos el punto de inicio y final como una tupla
print(span) #(0, 20)

comienzo, final = span
print(comienzo, final) #0, 20

substring = txt[comienzo:final]
print(substring) #Me encanta programar

mal_match = re.match('Me gusta programar', txt, re.I)
print(mal_match) #None - no encontro el substring

#Search
txt = '''Python es el lenguaje de programacion mas hermoso que el humano ha creado.
Recomiendo python como primer lenguaje de programacion'''

match = re.search('primer', txt, re.I)
print(match) #<re.Match object; span=(98, 104), match='primer'>
span = match.span()
comienzo, final = span
substring = txt[comienzo:final]
print(substring)
#SEARCH es mejor que MATCH ya que busca el patron a traves del texto. Retorna una coincidencia
#con la primer coincidencia que encontro, sino retorna None. 

#Una funcion mucho mejor de RE es FINDALL.
coincidencias = re.findall('lenguaje', txt, re.I)
print(coincidencias) #['lenguaje', 'lenguaje']

coincidencias = re.findall('python', txt, re.I)
print(coincidencias) #['Python', 'python']
#Como utilizamos re.I, capturamos palabras con o sin mayusculas. Si no utilizamos la flag, tendriamos
#que modificar el patron:
coincidencias = re.findall('Python|python', txt)
print(coincidencias) #Mismo resultado

coincidencias = re.findall('[Pp]ython', txt)
print(coincidencias) #Mismo resultado

#Reemplazar un substring con re.SUB
txt = '&Mi n&om&bre &es Ra&mi&ro Tu&les'
mejorado = re.sub('&', '', txt)
print(mejorado) #Mi nombre es Ramiro Tules

#Dividir texto con RegEx SPLIT
txt = '''Mi nombre es Ramiro Tules.
Soy programador y analista de datos.
Vivo en Mendoza, Argentina.'''
print(re.split('\n', txt)) #['Mi nombre es Ramiro Tules.', 'Soy programador y analista de datos', 'Vivo en Mendoza, Argentina.']

#Escribir patrones RegEx
#Para declarar un string utilizamos comillas simples o dobles, y para una variable RegEx, r'.
#El siguiente patron identifica 'manzana'
patron_regex = r'manzana'
txt = 'Manzana y banana son frutas. Una manzana contiene 52Kcal, 0,3g de proteinas, y 0,2g de grasa total'
coincidencias = re.findall(patron_regex, txt, re.I)
print(coincidencias) #['Manzana', 'manzana']

#[]: Conjunto de caracteres
#   [a-c]: a, b o c
#   [a-z]: cualquier letra desde a hasta z
#   [A-Z]: cualquier letra desde A hasta Z
#   [0-9]: cualquier numero desde 0 hasta 9
#   [A-Za-z0-9]: cualquier caracter, desde a hasta z, desde A hasta Z, o desde 0 hasta 9
#\: para capturar caracteres especiales
#   \d: coincide donde el string contenga digitos
#   \D: coincide donde el string no contenga digitos
#.: cualquier caracter excepto salto de linea (\n)
#^: comienza con
#   r'^python': oracion que comience con la palabra python
#   r'[^abc]': ni a, ni b, ni c
#$: termina con
#   r'python$': oracion que termine con la palabra python
#*: cero o mas veces
#   r'[a]*': a opcional, o puede ocurrir varias veces
#+: una o mas veces
#   r'[a]+': minimo una vez (o mas)
#?: cero o una vez
#   r'[a]?': cero o una sola vez
#{3}: exactamente 3 caracteres
#{3,}: minimo 3 caracteres
#{3,8}: de 3 a 8 caracteres
#|: o uno o el otro
#   r'manzana|banana' o manzana o banana
#(): capturar y agrupar

#1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
lista = re.split('\s',paragraph)
nueva = []
for i in lista:
    nueva.append((lista.count(i), i))
nueva2 = set(nueva)
nueva3 = sorted(nueva2)
print(nueva3)

#2. The position of some particles on the horizontal x-axis are -1, 2, -4, -3 and -1 in the negative direction, 0 at origin, 
# 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
puntos1 = [int(i) for i in points]
puntos1.sort()
diferencia = abs(puntos1[0]) + abs(puntos1[-1])
print(diferencia)

#3. Write a pattern which identifies if a string is a valid python variable
patron = r'^\D*_'

#4. Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;.
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple.
;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

oracion = re.sub(r'[^ a-zA-Z]','',sentence)
