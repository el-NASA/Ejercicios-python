from random import randint
lista = [randint(0, 10) for x in range(0, 20)]
pares = [x for x in lista if x % 2 == 0]
impares = [x for x in lista if x % 2 != 0]

print(lista)
print(pares, "la media es: ", sum(pares) / len(pares))
print(impares, "la media es: ", sum(impares) / len(pares))
