from op_octales import *


def main():
    num1, num2 = [int(x) for x in input("digite dos numeros: ").split()]
    num1 = octal(num1)
    num2 = octal(num2)

    print("los valores binarios de los numeros son {} y {} respectivamente".format(
        num1, num2))

    print("su suma es:", suma(num1, num2))
    print("su resta es:", resta(num1, num2))
    print("su multiplacion es:", mult(num1, num2))
    print("su division es:", div(num1, num2))


if __name__ == '__main__':
    main()
