Tamaño_1 = float(input("Ingrese tamaño de la esfera 1: "))
Tamaño_2 = float(input("Ingrese tamaño de la esfera 2: "))
Tamaño_3 = float(input("Ingrese tamaño de la esfera 3: "))
Peso_1 = float(input("Ingrese peso de la esfera 1: "))
Peso_2 = float(input("Ingrese peso de la esfera 2: "))
Peso_3 = float(input("Ingrese peso de la esfera 3: "))
Densi_1 = Peso_1 / Tamaño_1
Densi_2 = Peso_2 / Tamaño_2
Densi_3 = Peso_3 / Tamaño_3

if Densi_1 > Densi_2 and Densi_1 > Densi_3:
    print(f"La esfera 1 es la de mayor densidad: {Densi_1}")
elif Densi_2 > Densi_1 and Densi_2 > Densi_3:
    print(f"La esfera 2 es la de mayor densidad: {Densi_2}")
elif Densi_3 > Densi_1 and Densi_3 > Densi_2:
    print(f"La esfera 3 es la de mayor densidad: {Densi_3}")