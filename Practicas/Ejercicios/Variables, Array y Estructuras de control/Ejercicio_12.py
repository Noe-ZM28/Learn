def validar_cedula(cedula):
	cedula = cedula.replace('-','')
	if len(cedula)== 11:
		if (int(cedula[0:3]) < 122 and int(cedula[0:3]) > 0 or int(cedula[0:3]) == 402):
			suma = 0
			mutliplicador = 1
			verificador = 0
			mutliplicador = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
			for i in range(10):
				digito = int(cedula[i])*mutliplicador[i]
				if(digito>9):
					digito = digito//10 + digito%10
				suma = suma + digito
			verificador = (10 - (suma % 10) ) % 10
			if(verificador == int(cedula[10]) ):
				return True
			else:
				return False
		else:
			return False
	else:
		return False
cedula = "1234567890"
if validar_cedula(cedula) == True:
    print("La cedula es valida")
else:
    print("la cedula no es valida")
