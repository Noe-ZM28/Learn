from tkinter import *
from tkinter import messagebox

def verificar():

    if usuario.get == None:
        messagebox.showinfo('Error', 'Falto nombre de usuario')
    elif passs == None:
        messagebox.showinfo('Error', 'Falto contraseña')


ventana=Tk()
ventana.title("Login")
ventana.geometry("300x100")
user = StringVar()
password = StringVar()
user.set("Ingresa tu nombre de usuario")
password.set("Ingresa tu contraseña")

usuario = StringVar()
passs = StringVar()
etiqueta_user = Label(ventana, text = "Ingresa tu nombre de usuario").place(x=10, y = 10)
caja_usuario = Entry(ventana, textvariable = usuario, width = 10).place(x=180, y = 10)
etiqueta_contraseña = Label(ventana, text = "Ingresa tu contraseña").place(x=10, y = 30)
caja_contraseña = Entry(ventana, textvariable = passs,width = 10).place(x=180, y = 30)

mostrar = Radiobutton(ventana, text = "Mostrar contraseña").place(x=10, y = 60)
btn = Button(ventana, text = "Login", command = verificar).place(x=150, y = 60)

ventana.mainloop()
