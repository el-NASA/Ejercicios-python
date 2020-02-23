import time
horas, min, seg = [int(x) for x in input(
    "ingrese la hora, minutos y segundos separados por comas: ").split(',')]

seg_total = (horas * 3600) + (min * 60) + seg

start = time.time()
time.clock()
elapsed = 0
while elapsed <= seg_total:
    elapsed = time.time() - start
    horas = elapsed // 3600
    min = (elapsed % 3600) // 60
    seg = (elapsed % 3600) % 60
    # añadir al print el tiempo del ciclo loop cycle time: %f, time.clock()
    print ("horas: %d, minutos: %d, segundos: %d" % (horas, min, seg))
    time.sleep(1)
