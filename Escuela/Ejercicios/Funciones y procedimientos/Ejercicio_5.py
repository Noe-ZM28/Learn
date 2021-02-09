class renta_vehiculos():
    #
    def __init__(self, dias_alquiler, tipo_auto, vuelta_dias):
        self.dias_alquiler = dias_alquiler
        self.tipo_auto = tipo_auto
        self.vuelta_dias = vuelta_dias
        self.ALQUILER_DIA_AUTO = 1000
        self.ALQUILER_DIA_CAMIONETA = 1200
        self.MULTA_DIA = 150
        return
    #
    def calcular_multa(self):
        multa_total = 0
        if self.vuelta_dias > self.dias_alquiler:
            multa = self.vuelta_dias - self.dias_alquiler
            multa_total = multa * self.MULTA_DIA
            return multa_total
        else:
            return multa_total
    #
    def calcular_monto(self):
        costo_descuento = 0
        alquiler = 0
        if self.tipo_auto == 1:
            alquiler = self.ALQUILER_DIA_AUTO
        if self.tipo_auto == 1:
            alquiler = self.ALQUILER_DIA_CAMIONETA
        costo = alquiler * self.dias_alquiler
        if self.dias_alquiler >= 7:
            costo_descuento = costo * 0.25
        costo_total = costo + self.calcular_multa() + costo_descuento

        return costo_total

RV = renta_vehiculos(1, 1, 7)
print(RV.calcular_monto())
            
