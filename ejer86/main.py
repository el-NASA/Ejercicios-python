archivo = open("caracteres.txt", "w")
for i in range(0, 256):
    archivo.write(chr(i) + "\n")
archivo.close()
