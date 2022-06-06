# Solucion Reto 4
numeroPaquetes = int(input())
alto = float(input())
ancho = float(input())
profundo = float(input())
#Descuento = int(input("Descuento a apli2car "))
costoFinal = 0
costoTotal = 0



#def calcularCosto(alto, ancho, profundo):
    #costoTotal = 0
    #volumen = float(alto*ancho*profundo)
    #costo = float(volumen*5)
    #iva = float()
    #if (alto > 30):
        #costo = + 2000.0
    #if (costo > 10000.0):
        #iva = (costo * 0.19)

    #costo += iva
    #costoTotal += costo
    #return costoTotal


#def costoTotal(numeroPaquetes=(int(input()))):
    
    #return costoTotal, costoFinal



#print(costoTotal(numeroPaquetes))
for numeroPaquetes in range(numeroPaquetes):
        volumen = float(alto*ancho*profundo)
        costo = float(volumen*5)
        iva = float()
        if (alto > 30):
            costo = + 2000.0
        if (costo > 10000.0):
            iva = (costo * 0.19)

        costo += iva
        costoTotal += costo
        costoFinal = + costoTotal

print(costoFinal)

