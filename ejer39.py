i = 0
j = 20
opc = 1
while(opc == 1 and j <= 1000):
    for numero in range(i, j):
        print(numero, end=' ')
    i += 20
    j += 20
    opc = int(input("\nquiere seguir? (1: si, 0: no): "))
