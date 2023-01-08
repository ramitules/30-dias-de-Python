from tkinter import Tk, Label, ttk, messagebox

def callbackFunc(event):
    print("New Element Selected")

app = Tk()
app.geometry("200x100")

labelTop = Label(app, text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, values=["Enero", "Febrero", "Marzo", "Abril"], state='readonly')
comboExample.grid(column=0, row=1)
comboExample.current(0)
comboExample.bind("<<ComboboxSelected>>", callbackFunc)
# Con esto se crearia un menu desplegable.

messagebox.showinfo(message='Mensaje', title='Titulo de la ventana')
# Con eso se crearia un cuadro de dialogo. Es una ventana modal (no se permite hace nada a menos que se cierre el dialogo)
# Las funciones de interrogacion retornan True o False
# showinfo()
# showwarning()
# showerror()
# askquestion() retorna 'yes' o 'no'
# askyesno()
# askokcancel()
# askyesnocancel() retorna 'True', 'False' o 'None'
# askretrycancel()

app.mainloop()