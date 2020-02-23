def suma(num):
    if num == 0:
        return 0
    else:
        return num + suma(num - 1)


def main():
    num = int(input("digite un numero: "))
    print(suma(num))


if __name__ == '__main__':
    main()
