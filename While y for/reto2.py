#Solucion Reto # 2
numeropaquetes = int(input())
costoTotal = 0
for numerodepquetes in range(numeropaquetes):
    alto = float(input())
    ancho = float(input())
    profundo = float(input())
    volumen = float(alto*ancho*profundo)
    costo = float(volumen*5)
    iva = float()
    if (alto > 30):
        costo = (costo + 2000.0)
    if (costo > 10000.0):
        iva = (costo * 0.19)
    costo += iva
    costoTotal += costo
    print(volumen)
    print(costo)
print(costoTotal)
