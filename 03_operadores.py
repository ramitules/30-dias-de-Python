#OPERADORES
print (3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4)
print (4 % 2)
print (10 // 3)
print (3 ** 4)

print ("Rami" + "Tules")
print ("Hola " * 4)
print ("Ramiro" + str(25))

#OERADORES COMPARATIVOS
print (3 < 4)
print (3 > 4)
print (3 == 4)
print (3 != 4)
print (3 <= 4)

#OPERADORES LOGICOS
print (3 > 4 or "Hola" < "Chau")
print (3 < 4 and "Hola" >= "Chau")
print (not(3 > 4))

#1. Declare your age as integer variable

age = 25

#2. Declare your height as a float variable

height = 1.70

#3. Declare a variable that store a complex number

x = 1j

#4. Write a script that prompts the user to enter base and height of the triangle and calculate
# an area of this triangle (area = 0.5 x b x h)

base = int (input ("Base: "))
height = int (input ("Altura: "))
area = (0.5 * base * height)
print ("Area: ", area)

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle.
#Calculate the perimeter of the triangle (perimeter = a+b+c).

side_a = int (input ("Lado a: "))
side_b = int (input ("Lado b: "))
side_c = int (input ("Lado c: "))
perimeter = side_a + side_b + side_c
print("Perimetro: ", perimeter)


#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width)
# and perimeter (perimeter = 2 x (length + width)).

length = int (input ("Alto: "))
width = int (input ("Ancho: "))
area = length * width
perimeter = 2 * (length + width)
print ("Area: ", area, "- Perimetro: ", perimeter)

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and
# circumference (c = 2 x pi x r) where pi = 3.14

pi = 3.14
radius = float(input ("Radio: "))
area = pi * (radius * radius)
circumference = (2 * pi) * radius
print ("Area: ", area, "- Circunferencia: ", circumference)

#8. Calculate the slope, x-intercept and y-intercept of y = 2x-2


#9. Slope is (m = y2 - y1 / x2 - x1). Find the slope and Euclidean distance between
# point (2, 2) and point (6, 10)

x1 = int (2)
y1 = int (2)
x2 = int (6)
y2 = int (10)
m = (y2 - y1) / (x2 - x1)
euclidean = ((y1 - x1)**2) + ((y2 - x2)**2)
print (m, euclidean)

#10. Compare the slopes in tasks 8 and 9

#11. Calculate the value of y (y = x² + 6x + 9). Try to use different x values and figure
# out at what x value y is going to be 0.

a = int (1)
b = int (6)
c = int (9)
x1 = (-b+((b**2)-(4*a*c)))/2*a
x2 = (-b-((b**2)-(4*a*c)))/2*a
print (x1, x2)

#12. Find the length of "python" and "dragon" and make a falsy comparison statement.

print (not(len("python") == len("dragon")))

#13. Use AND operator to check if "on" is found in both "python" and "dragon"

print ("on" in "python" and "on" in "dragon")

#14. "I hope this course is not full of jargon". Use "in" operator to check if jargon
# is in the sentence.

print ("jargon" in "I hope this course is not full of jargon")

#15. There is no "on" in both dragon and python

#16. Find the length of the text "python" and convert the value to float and convert
# it to string

r = len("python")
print (float (r))
print (str (r))

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a
# number is even or not using python?
# USING "%" AND CONDITIONAL

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7

n = int (2.7)
print ((7 // 3)==n)

#19. Check if type of "10" is equal to type of 10

print (type("10")==type(10))

#20. Check if int("9.8") is equal to 10
# ITs NOT, LOL

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate
# pay of the person.

n = float (input("Horas: "))
r = float (input("Ganancia por hora: "))
print("Ganancias por semana: ", n*r)

#22. Write a script that prompts the user to enter number of years. Calculate the number
# of seconds a person can live. Assume a person can live a hundred years.

n = int (input("Cantidad de años que vivio: "))
print("Usted vivio ", n*31536000, " segundos")

#23. Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

n = int (2)
print (n**0, n**0, n**0, n**0, n**0)
print (n**1, n**0, n**1, n**2, n**3)
n+=1
print (n**1, n**0, n**1, n**2, n**3)
n+=1
print (n**1, n**0, n**1, n**2, n**3)
n+=1
print (n**1, n**0, n**1, n**2, n**3)
