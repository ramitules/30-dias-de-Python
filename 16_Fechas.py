#FECHA Y HORA EN PYTHON

#Python contiene un modulo llamado DATETIME para manipular fecha y hora

from datetime import datetime
print(dir(datetime))

#Obteniendo la fecha y hora actual
now = datetime.now()
print(now)
dia = now.day
mes = now.month
anio = now.year
hora = now.hour
minutos = now.minute
segundos = now.second
timestamp = now.timestamp()
print(dia, mes, anio, hora, minutos)
print('timestamp', timestamp) #La cantidad de segundos que pasaron desde el 1 de Enero de 1970 UTC
print(f'{dia}/{mes}/{anio}, {hora}:{minutos}')

anio_nuevo = datetime(2023, 1, 1)
print(anio_nuevo)

#Formatear fechas usando STRFTIME
ahora = datetime.now()
t = ahora.strftime('%H:%M:%S')
print("Hora:", t)

tiempo = now.strftime('%d/%m/%y, %H:%M:%S')
print(tiempo)

#Formatear fechas usando STRPTIME
string_fecha = '9 December, 2022'
print("String fecha: ", string_fecha)
objeto_fecha = datetime.strptime(string_fecha, '%d %B, %Y')
print("Objeto fecha: ", objeto_fecha)

#Objetos tiempo para representar horas
from datetime import time
a = time()
print('a: ', a)
b = time(10, 30, 50)
print('b: ', b)
c = time(hour = 10, minute = 30, second = 50)
print('c: ', c) #Igual al anterior
d = time(10, 30, 50, 200555) #Con microsegundos
print('d: ', d)

#Diferencia entre dos puntos en el tiempo con DATE
from datetime import date

hoy = date(2022, 12, 12)
anio_nuevo = date(2023, 1, 1)
hasta_anio_nuevo = anio_nuevo - hoy
print("Tiempo hasta que llegue anio nuevo: ", hasta_anio_nuevo)

t1 = datetime(2022, 12, 12, 0, 59, 0)
t2 = datetime(2023, 1, 1, 0, 0, 0)
diferencia = t2 - t1
print("Tiempo hasta que llegue anio nuevo: ", diferencia)

#Diferencia entre dos puntos en el tiempo con TIMEDELTA
from datetime import timedelta

t1 = timedelta(weeks = 12, days = 10, hours = 4, seconds = 20)
t2 = timedelta(days = 7, hours = 5, minutes = 3, seconds = 30)
t3 = t1 - t2
print(t3)