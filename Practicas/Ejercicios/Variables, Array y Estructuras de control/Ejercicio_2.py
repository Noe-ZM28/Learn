peso = float(input("Ingrese su peso corporal en Kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = (peso / altura**2)
estado = ""
if imc <18.49:
    estado = "Infrapeso"
elif imc >=18.50 and imc <= 24.99:
    estado = "Normal"
elif imc >=25 and imc <= 29.99:
    estado = "sobrepeso"
if imc <30:
    estado = "Obesidad"

print(f"Su IMC es: {imc}, su estado es {estado}")