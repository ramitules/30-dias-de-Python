from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title('Ejemplo de Treeview')
ventana.geometry('400x300')
ventana.config(bg='orange')

# Crear un Treeview
tv = ttk.Treeview(ventana)
tv.insert('', END, text='Elemento 1')
tv.pack()

ventana.mainloop()