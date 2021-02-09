materias = {
	"Matematicas":0,
	"Fisica":0,
	"Biologia":0,
	"Quimica": 0,
	"Derecho":0
	}
suma = 0
estado = ""
for materia in materias:
	nota_materia = float(input(f"Ingrese la calificación de {materia}: "))
	materias[materia] = nota_materia
	suma = suma + nota_materia
promedio = suma / len(materias)
if promedio >=1 and promedio <= 2:
	estado = "Examen en frebrero"
elif promedio >= 3 and promedio <= 6:
	estado = "Examen en diciembre"
elif promedio >= 7 and promedio <= 11:
	estado = "Aprueba"
elif promedio == 12:
	estado = "Aprueba con honores"

print("\n\n\t\tCalificaciones")
for materia in materias:
	print(f"{materia}:{materias[materia]}")

print(f"El promedio es: {promedio}")
print(f"Estado: {estado}")

