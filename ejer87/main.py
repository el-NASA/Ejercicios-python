archivo = open("caracteres.txt", "w")
for i in range(0, 256):
    archivo.write(chr(i) + "\n")
archivo.close()

archivo = open("caracteres.txt", "r")
caracteres = archivo.readlines()
archivo.close()
caracteres = [s.rstrip('\n') for s in caracteres]
for i in caracteres:
    print(i, end=' ')
