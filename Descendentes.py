A = int(input("Ingrese un numero: "))
B = int(input("Ingrese un numero: "))
C = int(input("Ingrese un numero: "))

if A > B and A > C:
    if B > C:
        print(f"Orden descendente: {A},{B},{C}")
    else:
        print(f"Orden descendente: {A},{C},{B}")
elif B > A and B > C:
    if A > C:
        print(f"Orden descendente: {B},{A},{C}")
    else:
        print(f"Orden descendente: {B},{C},{A}")
else:
    if A > B:
        print(f"Orden descendente: {C},{A},{B}")
    else:
        print(f"Orden descendente: {C},{B},{A}")
