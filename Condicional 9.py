A = int(input("Ingrese un numero: "))
B = int(input("Ingrese un numero: "))
C = int(input("Ingrese un numero: "))
D = int(input("Ingrese un numero: "))

mayor = A
if B > mayor:
    mayor = B
if C > mayor:
    mayor = C
if D > mayor:
    mayor = D

menor = A
if B < menor:
    menor = B
if C < menor:
    menor = C
if D < menor:
    menor = D

Suma = menor + mayor

print(f"Si se tiene los numero:{A},{B},{C} y {D}, la suma entre el menor y el mayor es: {menor + mayor} ")
