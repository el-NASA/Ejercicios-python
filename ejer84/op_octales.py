def octal(numero):
    a = format(numero, "o")
    return a


def suma(num1, num2):
    return format((int(num1, 8) + int(num2, 8)), "o")


def resta(num1, num2):
    return format((int(num1, 8) - int(num2, 8)), "o")


def mult(num1, num2):
    return format((int(num1, 8) * int(num2, 8)), "o")


def div(num1, num2):
    return format((int(num1, 8) - int(num2, 8)), "o")
