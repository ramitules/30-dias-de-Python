from tkinter import *

# Los frames son marcos contenedores de otros widgets. Pueden tener tamano propio y posicionarse en distintos lugares
# de otro contenedor (ya sea la raiz u otro marco).

ventana = Tk()
ventana.title("Hello world")
ventana.geometry("720x480")

frame1 = Frame(ventana, bg='grey') #Debe tener el master (ventana) y opciones de ser necesario
frame1.pack(expand=True, fill='both')
frame1.config(cursor='heart')
# width, height = tamano
# bg = color de fondo
# bd = grosor del borde
# relief = tipo de borde
# cursor = cursor

frame2 = Frame(ventana, bg='black')
frame2.pack(expand=True, fill='both')

ventana.mainloop()