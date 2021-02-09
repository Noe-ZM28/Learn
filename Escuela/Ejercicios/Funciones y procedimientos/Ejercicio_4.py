class inpuesto():
    def __init__(self, precio):
        self.precio = precio
        self.precio_iva = 0
    def calcular_iva(self):
        precio = self.precio
        self.precio_iva = precio * 0.16
        precio_final = precio + self.precio_iva
        return precio_final
articulo = int(input("Ingrese el precio de un articulo: "))
I = inpuesto(articulo)
print(f"Precio inicial: {I.precio}")
print(f"Precio del iva: {I.precio_iva}")
print(f"Precio final: {I.calcular_iva()}")

