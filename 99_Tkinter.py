from tkinter import *

# Metodos principales
#   Tk(): ventana principal
#   pack(): ubica los widgets en una posicion
#   mainloop(): inicia el bucle y monitorea la interaccion del usuario

ventana = Tk()
ventana.title("Hello world")    #Titulo principal de la ventana
ventana.geometry("720x480")     #Tamaño de la ventana

lbl = Label(ventana, text = "Este es un label")     #Se crea un texto o etiqueta

def bienvenida():
    print("Hola!")

btn = Button(ventana, text = "Presionar", command = bienvenida)    #Se crea un boton

# Se pueden configurar widgets de 3 maneras
#   Constructor (realizado anteriormente)

#   Metodo config
btn.config(fg = "black", bg = "white")

#   Accediendo a la propiedad
btn["fg"] = "black"

# Definir el modo en que deben colocarse los widgets dentro de una ventana
#   place: ubica elementos de forma absoluta indicando su posicion X e Y respecto de un elemento padre
#btn.place(x=60, y=40, width=100, height=30) #Posicion absoluta
#btn.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.5) #Posicion relativa tipo porcentaje

#   pack: ubica elementos de forma relativa respecto a algun contenedor, sin coordenadas. Por defecto los ubica uno bajo el otro
caja = Entry(ventana)
caja.pack(side = 'right') #Con side establecemos la ubicacion (top, bottom, left, right)
lab = Label(ventana, text = "Una caja")
lab.pack(side = "right", after = caja) #Con after o before lo ubicamos despues o antes de otro widget
btn2 = Button(ventana, text = "CAJA")
btn2.pack(side="right", padx = 10, ipadx = 10) #Con pad e ipad establecemos margenes externos e internos (X e Y)
#expand: establece si el elemento se expande o no con la ventana (True o False)
#fill: mismo que expand, pero se puede especificar X Y o BOTH


#   grid

# Para construir las ventanas se pueden utilizar unos widgets especiales (marcos, paneles, etc.)
# que actuan como contenedores de otros widgets. Se utilizan para agrupar varios controles.
# No deben mezclarse distintos metodos dentro de un mismo contenedor


ventana.mainloop()  #Bucle principal

