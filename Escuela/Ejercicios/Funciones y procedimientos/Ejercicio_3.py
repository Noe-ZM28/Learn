class Largo():
    def __init__(self, numero):
        self.numero = numero
    def longitud(self):
        texto = str(self.numero)
        largo = len(texto)
        return largo
numero = int(input("Ingresa un numero: "))
L = Largo(100)
print(L.longitud())