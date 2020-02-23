def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def main():
    num = int(input("digite un numero: "))
    print(fibonacci(num))


if __name__ == '__main__':
    main()
