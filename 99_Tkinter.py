from tkinter import *

# Metodos principales
#   Tk(): ventana principal
#   pack(): ubica los widgets en una posicion
#   mainloop(): inicia el bucle y monitorea la interaccion del usuario

ventana = Tk()
ventana.title("Hello world")    #Titulo principal de la ventana
ventana.geometry("720x480")     #Tamaño de la ventana

lbl = Label(ventana, text = "Este es un label")     #Se crea un texto o etiqueta
lbl.pack()

def bienvenida():
    print("Hola!")

btn = Button(ventana, text = "Presionar", command = bienvenida)    #Se crea un boton
btn.pack()

# Se pueden configurar widgets de 3 maneras
#   Constructor (realizado anteriormente)

#   Metodo config
btn.config(fg = "black", bg = "white")

#   Accediendo a la propiedad
btn["fg"] = "black"

# Para construir las ventanas se pueden utilizar unos widgets especiales (marcos, paneles, etc.)
# que actuan como contenedores de otros widgets. Se utilizan para agrupar varios controles.
# No deben mezclarse distintos metodos dentro de un mismo contenedor

ventana.mainloop()  #Bucle principal

