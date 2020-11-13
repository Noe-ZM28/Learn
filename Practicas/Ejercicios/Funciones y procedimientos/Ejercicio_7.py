class reloj():
    def __init__(self, entrada, salida):
        self.entrada = entrada
        self.salida = salida
        self.hora_entrada = 7
        self.hora_salida = 17
        self.mensaje_entrada = ""
        self.mensaje_salida = ""
        
    def calcular(self):
        if self.entrada > self.hora_entrada:
            self.mensaje_entrada = "Entrada despues de la hora"
        else:
            self.mensaje_entrada = "Entrada antes de la hora"

        if self.salida > self.hora_entrada:
            self.mensaje_salida = "Salida despues de la hora"
        else:
            self.mensaje_salida = "Dalida antes de la hora"
        horas_trabajadas = self.salida - self.entrada
        print(f"{self.mensaje_entrada}.\n{self.mensaje_salida}.\nHoras trabajadas: {horas_trabajadas}")

R = reloj(8, 15)
R.calcular()