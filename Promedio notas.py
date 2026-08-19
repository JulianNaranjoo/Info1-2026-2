Nota1 = float(input("Ingrese nota 1: "))
Nota2 = float(input("Ingrese nota 2: "))
Nota3 = float(input("Ingrese nota 3: "))
Nota4 = float(input("Ingrese nota 4: "))
Nota5 = float(input("Ingrese nota 5: "))

Promedio = (Nota1 * 0.3) + (Nota2 * 0.15) + (Nota3 * 0.15) + (Nota4 * 0.20) + (Nota5 * 0.20)

print("Las notas de un curso estan ponderadas de la siguiente manera: Nota 1: 30%, Nota 2: 15%, Nota 3: 15%, Nota 4: 20%  , Nota 5: 20% \nSi las notas obtenidas son: \nNota 1: {} \nNota 2: {} \nNota 3: {} \nNota 4: {} \nNota 5: {} \nEl promedio es: {} ".format(Nota1, Nota2, Nota3, Nota4, Nota5, Promedio))
