import json
with open("paquetes.json") as informacion:
    empresa = json.load(informacion)

def calcularCosto(alto,ancho,profundo):
    volumen = (alto*ancho*profundo)
    costo = (volumen*5)
    if alto > 30:
        costo = costo + 2000
    if costo > 10000:
        costo = costo + costo*0.19
    return costo
       

def costoTotal(listapquetes, descuento):
    tam = len(listapquetes)
    costo_Total = 0
    #numeroPaqutes = int(input("Ingrese el numero de paquetes"))
    for i in range(listapquetes):
        alto = float()
        ancho = float()
        profundo = listapquetes[pa]
        costo_Total = costo_Total + calcularCosto(alto,ancho,profundo)*(1-descuento/100)
    return costo_Total

    print(empresa)
    print(empresa["PAQUETES"])
def calcularCosto(alto, ancho, profundo):
    volumen = alto*ancho*profundo
    costo = volumen*5

    if(alto>30):
        costo += 2000
    if(costo>10000):
        costo = costo + costo*0.19

    return costo

def costoTotal(listaPaquetes,descuento):
    tam = len(listaPaquetes)
    costoT = 0
    for paquete in range(tam):
        alto = listaPaquetes[paquete]["ALTO"]
        ancho = listaPaquetes[paquete]["ANCHO"]
        profundo = listaPaquetes[paquete]["PROFUNDO"]
        costo = calcularCosto(alto, ancho, profundo)
        #costoT += costo
        costoT = costoT + costo
    costoT = costoT - costoT*(descuento/100)
    return costo

x = input()
print(x)
print(len(x))