horas, min, seg = [int(x) for x in input(
    "ingrese la hora, minutos y segundos separados por comas: ").split(',')]

seg_total = (horas * 3600) + (min * 60) + seg

seg_total += int(input("digite el numero de segundos extra :"))

horas = seg_total // 3600
min = (seg_total % 3600) // 60
seg = (seg_total % 3600) % 60
print("la nueva hora será: ", horas, ",", min, ",", seg)
