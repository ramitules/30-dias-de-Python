from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title('Ejemplo de Treeview')
ventana.geometry('800x400')
ventana.config(bg='orange')

# Crear un Treeview
tv = ttk.Treeview(ventana)

item1 = tv.insert('', END, text='Elemento 1', open=1)
tv.insert(item1, END, text='Sub-elemento 1')

item2 = tv.insert('', END, text='Elemento 2')
tv.insert(item2, END, text='Sub-elemento 2')

print(tv.item(item1)) # Devuelve diccionario con valores de item1
print(tv.get_children()) # Devuelve lista con items
print(tv.get_children(item1)) # Devuelve lista con subitems

for x in tv.get_children():
    print(x)
    print(tv.get_children(x))

tv.pack(side='left')

tv2 = ttk.Treeview(ventana, columns=('C1','C2'))

tv2.column('#0', width=80)
tv2.column('C1', width=80, anchor=CENTER)
tv2.column('C2', width=80, anchor=CENTER)

tv2.heading('#0', text='Producto', anchor=CENTER)
tv2.heading('C1', text='Precio', anchor=CENTER)
tv2.heading('C2', text='Cantidad', anchor=CENTER)

tv2.insert('', END, text='Remera', values=('900','5'))
tv2.insert('', END, text='Pantalon', values=('9000','5'))

tv2.pack(side='right')

ventana.mainloop()