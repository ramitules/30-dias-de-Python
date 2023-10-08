from tkinter import *

ventana = Tk()

texto = Text(width='15', height='8') # Crea un texto largo
texto.pack()


scroll = Scrollbar(ventana) # Crea una barra de desplazamiento
scroll.pack(side='right', fill='y')

lista = Listbox(ventana, yscrollcommand=scroll.set) # Crea una caja de texto tipo lista
# e inserta la barra de desplazamiento
for x in range(100):
    lista.insert(END, 'Esta linea es numero' + str(x))

lista.pack(side='left', fill='both')
scroll.config(command=lista.yview) # Ejecuta una vista en vertical para el objeto 'lista'


def seleccionar():
    monitor.config(text=f'Opcion {opcion.get()}')

opcion = IntVar()

# Creamos botones circulares seleccionables, como opciones
Radiobutton(ventana, text='Opcion 1', variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(ventana, text='Opcion 2', variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(ventana, text='Opcion 3', variable=opcion, value=3, command=seleccionar).pack()

monitor = Label(ventana)
monitor.pack(side='bottom')

ventana.mainloop()