Y = float(input("Ingrese un numero: "))
Z = float(input("Ingrese un numero: "))

if Y > Z:
    X = 1
elif Y == Z:
    X = 2
else:
    X = 3
print(f"Si Y: {Y} y Z: {Z}, el valor de X es: {X}")
