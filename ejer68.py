def cuadrado(num):
    return num**2


def doble(num):
    return num * 2


def operacion(num):
    return cuadrado(num) - doble(num)


def main():
    num = int(input("digite un numero: "))
    print("el resultado de restar el doble al cuadrado es: ", operacion(num))


if __name__ == '__main__':
    main()
