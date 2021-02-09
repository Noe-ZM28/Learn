class conversion():
    grados = None
    def __init__(self, grados):
        self.grados = grados

    def celsius(self):
        celsius_ = self.grados
        fahrenheit = ((celsius_ * 9)/2)+32
        return fahrenheit
F = conversion(0)
print(F.celsius())
