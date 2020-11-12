
hora_entrada = int(input("Ingrese la hora de entrada: "))

if hora_entrada >= 7 and hora_entrada <= 10:
    comida = {
        "Huevos revueltos": 52,
        "Cafe y pan": 23,
        "Chilaquires verdes": 55
    }
    for platillo in comida:
        print(f"{platillo}:{comida[platillo]}")
elif hora_entrada > 10 and hora_entrada <= 15:
    comida = {
        "fruta": 32,
        "Tostadas": 30,
        "Pan con queso": 55
    }
    for platillo in comida:
        print(f"{platillo}:{comida[platillo]}")
elif hora_entrada > 15 and hora_entrada <= 19:
    comida = {
        "Guisado del dia": 52,
        "Espagueti": 23,
        "Guarniciones": 55
    }
    for platillo in comida:
        print(f"{platillo}:{comida[platillo]}")
elif hora_entrada > 19 and hora_entrada <= 23:   
    comida = {
        "Pan con cafe": 52,
        "Chilaquires": 23,
        "Polo con crema": 55
    }
    for platillo in comida:
        print(f"{platillo}:{comida[platillo]}")
else:
    print("Estamos cerrados. vuelva despues")