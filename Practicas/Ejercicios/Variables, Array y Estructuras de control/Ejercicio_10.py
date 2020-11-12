from tkinter import *
from tkinter import messagebox
Texto_actual = ""
def verificar():
    Texto_actual = Texto.get()
    tamaño = len(Texto_actual)
    etiqueta = Label(ventana, text = f"Su tamaño es {tamaño}").place(x = 10, y = 30)
    etiqueta_2 = Label(ventana, text = f"Texto actual: {Texto_actual}").place(x = 10, y = 50)

def minusculas():
    Texto_actual = Texto_actual.lower()

def mayusculas():
    Texto_actual = Texto_actual.upper()

ventana=Tk()
ventana.title("Texto")
ventana.geometry("300x300")

Texto = StringVar()

caja_texto = Entry(ventana, textvariable = Texto, width = 30).place(x=10, y = 10)
variable_texto = ""
btn = Button(ventana, text = "Cargar texto", command = verificar).place(x=210, y = 10)
Mayusculas = Radiobutton(ventana, text = "Mayusculas", command = mayusculas).place(x = 210, y = 20)
Minusculas = Radiobutton(ventana, text = "Minusculas", command = minusculas).place(x = 210,y =  40)
ventana.mainloop()