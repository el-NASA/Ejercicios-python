t, opc = input("ingrese la temperatura en grados c o f: ").split()
if opc == 'c':
    conversion = ((9 / 5) * float(t)) + 32
    print("la temperatura es: ", conversion, "f")
elif opc == 'f':
    conversion = ((5 / 9) * (float(t) - 32))
    print("la temperatura es: ", conversion, "c")
else:
    print("opcion no valida")
