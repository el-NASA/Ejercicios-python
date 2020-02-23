def distancia(x1, y1, x2, y2):
    return (((x2 - x1)**2) + ((y2 - y1)**2))**(1 / 2)


def main():
    x1, y1 = [int(x)
              for x in input("digite la primera coordenada: ").split(',')]
    x2, y2 = [int(x)
              for x in input("digite la segunda coordenada: ").split(',')]
    print("la distancia es: ", distancia(x1, y1, x2, y2))


if __name__ == "__main__":
    main()
