class vuelta():
    def __init__(self, numero):
        self.numero = numero
    def original(self):
        return self.numero
    def voltear(self):
        text_numero = str(self.numero)
        vuelta = ""
        for i in reversed(text_numero):
            vuelta = vuelta + i
        return vuelta

V = vuelta(1234)
print(V.original())
print(V.voltear())