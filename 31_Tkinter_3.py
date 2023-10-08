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

# Creacion de una ventana a traves de POO
class aplicacion(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side = 'top')

        self.quit = Button(self, text = 'Salir', fg = 'red', command = self.master.destroy)
        self.quit.pack(side = 'bottom')

    def say_hi(self):
        print('wenasss')

root = Tk()
root.wm_title('Mi aplicacion') # Se le agrega wm_ en caso de crear con clases
app = aplicacion(root)

root.mainloop()