Numero_I = int(input("Ingrese el numero de inscripción: "))
Nombre = str(input("Ingrese el nombre del estudiante: "))
Pat = int(input("Ingrese el valor del patrimonio: "))
Estrato = int(input("Ingrese el estrato: "))
Matricula = 50000

if Pat > 2000000 and Estrato > 3:
    Matricula = Matricula + (Pat * 0.03)

print(f"Número de inscripción: {Numero_I} \nNombres: {Nombre} \nPago de matricula: ${Matricula:,.0f}")
