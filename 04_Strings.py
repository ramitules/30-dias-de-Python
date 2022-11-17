# STRINGS

my_string = "Mi string"
other_string = "Otro string"

print (my_string + " " + other_string)

new_line = "String con \nsalto de linea"
print (new_line)

new_tab = "string con \t tabulacion"
print (new_tab)

multiline_string = '''I am a teacher and enjoy teaching people.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python'''
print (multiline_string)

print("This is a \"program\"")

# FORMATEO

name, surname, age = "Ramiro", "Tules", 25
print ("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print ("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print (f"Mi nombre es {name} {surname} y mi edad es {age}")

# DESEMPAQUETADO DE CARACTERES

language = "Python"
a, b, c, d, e, f = language
print (a)
print (e)

# DIVISION

language_slice = language[1:3]
print (language_slice)

language_slice = language[-2]
print (language_slice)

language_slice = language[0:6:2]
print (language_slice)

# REVERSION

reversed_language = language[::-1]
print (reversed_language)

# FUNCIONES

hola = "hola"
print (hola.capitalize())
print (hola.upper())
print (hola.count("h"))
print (hola.isnumeric())
print (hola.lower())
print (hola.upper().isupper())

#1. Concatenate the string "Thirty","Days","Of","Python" to a single string, "Thirty
# Days Of Python"

aa = "Thirty "
ab = "days "
ac = "of "
ad = "Python"
todo = aa + ab + ac + ad
print (todo)

#2. Concatenate the string "Coding", "for", "all" to a single string, "Coding for all"

aa = "Coding "
ab = "for "
ac = "all"
todo = aa + ab + ac
print (todo)

#3. Declare a variable named company and assign it to an initial value "Coding for all"

from gettext import find


company = "Coding for all"

#4. Print the variable company using print().

print (company)

#5. Print the length of the company string using len() method and print().

print(len(company))

#6. Change all the characters to uppercase letters using upper() method.

print (company.upper())

#7. Change all the characters to lowercase letters using lower() method.

print (company.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string
# Coding For All.

print (company.capitalize().title().swapcase())

#9. Cut(slice) out the first word of Codign For All string.

sliced = company[6:]
print (sliced)

#10. Check if Coding For All string contains a word Coding using the method index, find
# or other methods.

print(company.find("Coding"))

#11. Replace the wotd coding in the string "Coding for all" to "Python"

print(company.replace("Coding","Python"))

#12. Change Python for Everyone to Python for all using the replace method or other
# methods.

str1 = "Python for Everyone"
print (str1.replace("for Everyone", "for All"))

#13. Split the string "Coding for all" using space as the separator (split()).

print (company.split())

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at
# the coma

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))

#15. What is the character at index 0 in the string Coding For All

print(company[0])

#16. What is the last index of the string Coding for all

print (company[-1])

#17. What character is at index 10 in "Coding for all" string

print (company[10])

#18. Create an acronym or an abbreviation for the name "Python for everyone"

print(str1[0], str1[7], str1[11])

#19. Create an acronym or an abbreviation for the name "Coding for all"

print (company[0], company[-3])

#20. Use index to determine the position of the first occurrence of C in Coding for all

print (company.index("C"))

#21. Use index to determine the position of the first occurrence of F in Coding For All.

print (company.index("f"))

#22. Use rfind to determine the position of the last occurrence of l in Coding For All 
# People.

print (company.rfind("l"))

#23. Use index or find to find the position of the first occurrence of the word 
# 'because' in the following sentence: 'You cannot end a sentence with because 
# because because is a conjunction'

paragraph = 'You cannot end a sentence with because because because is a conjunction'
print (paragraph.index("because"))

#24. Use rindex to find the position of the last occurrence of the word because
#  in the following sentence: 'You cannot end a sentence with because because 
# because is a conjunction'

print (paragraph.rfind("because"))

#25. Slice out the phrase 'because because because' in the following 
# sentence: 'You cannot end a sentence with because because because is a conjunction'

print (paragraph[31:54])

#26. Does "Coding for all" start with a substring Coding?

print (company.startswith("Coding"))

#27. Does "Coding for all" end with a substring coding?

print (company.endswith("coding"))

#28. "  Coding for all  ", remove the left and right trailing spaces in the given str.

company2 = "    Coding for all  "
print(company2.strip(" "))

#29. Which one of the following variables return True when we use the method
#  isidentifier(): 30DaysOfPython - thirty_days_of_python

one = "30DaysOfPython"
two = "thirty_days_of_python"
print (one.isidentifier())
print (two.isidentifier())

#30. The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash 
# with space string.

lists = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = "# ".join(lists)
print (result)

#31. Use the new line escape sequence to separate the following sentences. 

p1 = "I am enjoying this challenge."
p2 = "I just wonder what is next."
print ("",p1,"\n",p2)

#32. Use a tab escape sequence to write the following lines.
# Name      Age     Country     City
# Asabeneh  250     Finland     Helsinki

print("Name\t Age\tCountry\t  City")
print("Asabeneh 250\tFinland\t  Helsinki")

#33. Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
print ("The area of a circle with radius {} is {}".format(radius, area))

#34. Make the following using string formatting methods:

a = 8
b = 6
print ("{} + {} =".format(a, b),a + b)
print ("{} - {} =".format(a, b),a - b)
print ("{} * {} =".format(a, b),a * b)
print ("{} / {} =".format(a, b),a / b)
print ("{} % {} =".format(a, b),a % b)
print ("{} // {} =".format(a, b),a // b)
print ("{} ** {} =".format(a, b),a ** b)