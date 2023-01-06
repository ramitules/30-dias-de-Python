from tkinter import *

ventana = Tk()
ventana.title("Hello world")
ventana.geometry("720x480")

# Definir el modo en que deben colocarse los widgets dentro de una ventana

#   PLACE: ubica elementos de forma absoluta indicando su posicion X e Y respecto de un elemento padre
btn.place(x=60, y=40, width=100, height=30) #Posicion absoluta
btn.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.5) #Posicion relativa tipo porcentaje

#   PACK: ubica elementos de forma relativa respecto a algun contenedor, sin coordenadas. Por defecto los ubica uno bajo el otro
caja = Entry(ventana)
caja.pack(side = 'right') #Con side establecemos la ubicacion (top, bottom, left, right)
lab = Label(ventana, text = "Una caja")
lab.pack(side = "right", after = caja) #Con after o before lo ubicamos despues o antes de otro widget
btn2 = Button(ventana, text = "CAJA")
btn2.pack(side="right", padx = 10, ipadx = 10) #Con pad e ipad establecemos margenes externos e internos (X e Y)
#expand: establece si el elemento se expande o no con la ventana (True o False),
#va acompañado de fill (BOTH, X, Y)

#   GRID: permite dividir la ventana en una grilla, donde la primer fila es row 0 y primer columna es column 0
caja = Entry(ventana)
caja.grid(row = 0, column = 0)
label = Label(ventana, text = '<-- una caja')
label.grid(row = 0, column = 1)
boton = Button(ventana, text = 'Presione aqui')
boton.grid(row = 1, column = 0)
#columnspan y rowspan expanden las columnas y/o filas utilizadas por el widget (por defecto 1)
#columnconfigure y rowconfigure con el parametro weight=1 indican que se expanden si la ventana se expande
#sticky se utiliza para posicionar el widget en la celda. 'n' norte, 's' sur, 'e' este, 'w' oeste. Se pueden combinar
#Tambien se pueden utilizar los pads
