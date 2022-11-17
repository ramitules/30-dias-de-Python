#LISTAS
"""
Lista: es una coleccion de diferentes tipos de datos, que esta ordenada y puede modificarse. Permite miembros duplicados.
Tupla: es una coleccion que esta ordenada y no puede modificarse. Permite miembros duplicados.
Conjunto: es una coleccion que NO esta ordenada, ni indexada, y no puede modificarse, pero podemos anadir nuevos items. No permite miembros duplicados.
Diccionario: es una coleccion que NO esta ordenada, puede modificarse y esta indexada. No permite miembros duplicados.


empty_list = list() #Lista vacia
empty_list2 = [] #Lista vacia tambien
print(len(empty_list)) #Da cero

print('\n')

fruits = ['Banana','Naranja','Mango','Manzana']
vegetables = ['Tomate','Lechuga','Papa','Batata','Cebolla']
print('Frutas: ', fruits)
print('Cantidad de frutas: ',len(fruits))

print('\n')

#Las listas pueden contener diferentes tipos de datos
lista1 = ['Ramiro','Tules','25',{'country':'Argentina','city':'Mendoza'}]

#Se puede acceder al indice en una lista a traves de numeros positivos o negativos
first_fruit = fruits[0]
print(first_fruit)
last_vegetable = vegetables[-1]
print(last_vegetable)

print('\n')

first_item, second_item, *rest = vegetables
print(first_item, second_item, rest)

print('\n')

#Se pueden modificar los items en las listas
vegetables[0] = 'Palta'
print (vegetables)

print('\n')

#Chequear que un item este en una lista con el operador IN
existe = 'Banana' in fruits
print(existe) #True

#Agregar un item al final de la lista con .APPEND()
fruits.append('Pera')
print(fruits)

print('\n')

#Se pueden insertar items a una lista con .INSERT(indice, item). Se corren los demas items a la derecha
vegetables.insert(3,'Choclo')
print(vegetables)

print('\n')

#Remover items con .REMOVE(item)
vegetables.remove('Lechuga')
print(vegetables)

print('\n')

#Remover items con .POP(indice), se especifica el indice, de lo contrario elimina el ultimo item
fruits.pop(2)
print(fruits)

print('\n')

#Remover listas enteras o items dentro de un rango con DEL
del vegetables[1:3]
print(vegetables)

del vegetables

print('\n')

#Limpiar una lista con .CLEAR()
fruits.clear()
print(fruits)

print('\n')

#Se pueden crear referencias a listas con "=" y asi cualquier modificacion que se le haga a la referencia, se le hace a la lista en si.
#Pero si se quiere crear una copia, se utiliza .COPY()
fruits = ['Banana', 'Manzana', 'Pera', 'Durazno']
copia_fruits = fruits.copy()
print(copia_fruits)

print('\n')

#Se pueden unir listas con el operador "+"
positivos = [1, 2, 3, 4]
negativos = [-1, -2, -3, -4]
cero = [0]
integrales = negativos + cero + positivos
print(integrales)

print('\n')

#Contar items en una lista con .COUNT(item)
edades = [19, 22, 32, 22, 40, 29, 22]
print(edades.count(22)) #3

print('\n')

#Buscar el indice de un item con .INDEX(item)
print(edades.index(40))

print('\n')

#Dar vuelta una lista con .REVERSE()
integrales.reverse()
print(integrales)

print('\n')

#Para ordenar una lista se utiliza .SORT() de forma ascendente. Tambien se puede ordenar de forma descendente con .SORT(reverse=true). Modifica la lista original
edades.sort()
print(edades)

print('\n')

#A su vez, se podria ordenar una lista sin necesidad de modificarla, con .SORTED(). Se puede ordenar de forma descendente
edades = sorted(edades,reverse=True)
print(edades)

print('\n')
"""
#1. Declarar una lista vacia.

lista_vacia = list()

#2. Declarar una lista con mas de 5 items

lista6 = [1, 2, 3, 4, 5, 6]

#3. Buscar la longitud de la lista

longitud = len(lista6)

#4. Buscar el primer item, el del medio, y el ultimo de la lista

print(lista6[0])
print(lista6[3])
print(lista6[len(lista6)-1])

#5. Declarar una lista llamada mixed_data_types, escribir (nombre, edad, altura, estado civil, direccion)

mixed_data_types = ['Ramiro', '25', '1.68', 'Soltero', 'Calle Corrientes 1656']

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7. Print the list using print()

print(it_companies)

#8. Print the number of companies in the list

print(len(it_companies))

#9. Print the first, middle and last company

print(it_companies[0], it_companies[int(len(it_companies)/2)], it_companies[-1])

#10. Print the list after modifying one of the companies

it_companies[0] = 'Tules'
print(it_companies)

#11. Add an IT company to it_companies

it_companies.append('Rockstar coders')

#12. Insert an IT company in the middle of the companies list

it_companies.insert(int(len(it_companies)/2),'Maxis')

#13. Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[1] = it_companies[1].upper()

#14. Join the it_companies with a string '#;  '

union = '#; '.join(it_companies)

#15. Check if a certain company exists in the it_companies list.

print('Microsoft' in it_companies)

#16. Sort the list using sort() method

it_companies.sort()

#17. Reverse the list in descending order using reverse() method

it_companies.reverse()

#18. Slice out the first 3 companies from the list

pedazo = it_companies[::3]

#19. Slice out the last 3 companies from the list

pedazo = it_companies[-3::]

#20. Slice out the middle IT company or companies from the list

pedazo = it_companies[int(len(it_companies)/2)]
print(pedazo)

#21. Remove the first IT company from the list

it_companies.pop(0)

#22. Remove the middle IT company or companies from the list

it_companies.pop(int(len(it_companies)/2))

#23. Remove the last IT company from the list

it_companies.pop()

#24. Remove all IT companies from the list

it_companies.clear()

#25. Destroy the IT companies list

del it_companies

#26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack.insert(full_stack.index('Redux')+1,'Python')
full_stack.insert(full_stack.index('Python')+1,'SQL')
print(full_stack)

#NIVEL 2

#1. The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#    Sort the list and find the min and max age

ages.sort()
min_age = ages[0]
max_age = ages[-1]

#    Add the min age and the max age again to the list

ages.append(min_age)
ages.append(max_age)
ages.sort()

#    Find the median age (one middle item or two middle items divided by two)

print(ages[int(len(ages)/2)])

#    Find the average age (sum of all items divided by their number )

promedio = sum(ages)/len(ages)

#    Find the range of the ages (max minus min)

rango = max_age - min_age

#    Compare the value of (min - average) and (max - average), use abs() method

print(abs(max_age-promedio), abs(min_age-promedio))

#2. Find the middle country(ies) in the countries list

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

middle_country = countries[int(len(countries)/2)]

#2. Divide the countries list into two equal lists if it is even if not one more country for the first half.

mitad1 = countries[0:int(len(countries)/2)]
mitad2 = countries[int(len(countries)/2)::]

#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

lista_aux = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
uno, dos, tres = lista_aux[0:3]
scandic_countries = lista_aux[3::]
