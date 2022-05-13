tabla_multiplicar = int(input("Ingrese un numero"))
tabla_final = int(input("Ingrese hasta donde desea multiplicar"))
iteraPro = 0
#for para iterar 10 veces
for i in range(0, tabla_final):
    iteraPro = iteraPro+tabla_multiplicar
    print(tabla_multiplicar, 'x', i+1, '=',iteraPro)