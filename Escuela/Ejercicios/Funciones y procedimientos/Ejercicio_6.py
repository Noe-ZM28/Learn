from tkinter import *
from tkinter import ttk, messagebox
ventana = Tk()
ventana.title("Lista")
ventana.geometry("300x200")
a1 = 10
a2= 30
a3 = 40
a4 = 80
a5 = 98
cantidad = IntVar()
def comando():
    if lista.get() == "Articulo 1":

        messagebox.showinfo("Resultado", f"Articulo: {lista.current()}, cantidad {2}, total 20")
opciones = [
            "Articulo 1",
            "Articulo 2",
            "Articulo 3",
            "Articulo 4",
            "Articulo 5"]
lista = ttk.Combobox(ventana, width = 20)
lista.place(x = 10, y = 10)
lista["values"] = opciones
cantidad = Label(ventana, text= "Catidad").place(x = 10, y = 35)
Button(ventana, text="Seleccionar", command= comando).place(x = 165, y = 7)
caja = Entry(ventana, textvariable = cantidad).place(x = 100, y = 38)
ventana.mainloop()