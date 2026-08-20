Nota_1 = float(input("Ingrese Nota 1: "))
Nota_2 = float(input("Ingrese Nota 2: "))
Nota_3 = float(input("Ingrese Nota 3: "))
Nota_4 = float(input("Ingrese Nota 4: "))
Nota_5 = float(input("Ingrese Nota 5: "))
Promedio = (Nota_1 * 0.3) + (Nota_2 * 0.15) + (Nota_3 * 0.15) + (Nota_4 * 0.2) + (Nota_5 * 0.2)

print(f"Nota 1: {Nota_1} \nNota 2: {Nota_2} \nNota 3: {Nota_3} \nNota 4: {Nota_4} \nNota 5: {Nota_5} \nPromedio: {Promedio}")
if Promedio >= 3:
    print("Aprovado")
else:
    print("Reprovado")
    