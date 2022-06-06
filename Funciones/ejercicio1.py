def calcularCosto(alto,ancho,profundo):
    volumen = (alto*ancho*profundo)
    costo = (volumen*5)
    if alto > 30:
        costo = costo + 2000
    if costo > 10000:
        costo = costo + costo*0.19
    return costo
       
def costoTotal(numeroPaquetes, descuento):
    costo_Total=0
    for i in range(numeroPaquetes):
        alto = float(input())
        ancho = float(input())
        profundo = float(input())
        costo_Total = costo_Total + calcularCosto(alto,ancho,profundo)*(1-descuento/100)
    return costo_Total

print(calcularCosto(12,222,22))
print(costoTotal(2,34))