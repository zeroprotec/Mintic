
Salario = int(input("Ingrese le salario SMMLV "))
Arl = (input("Ingrese el nivel de riesgo, solo numeros "))
valorArl = int()
Ibc = int(Salario * 0.4)
salud = (Ibc * 0,125)
pension = (Ibc * 0,16)
total = ()

if Salario >= 1000000:
    if Arl == 1:
        valorArl = Ibc * 0.00552 
    elif Arl == 2:
        valorArl = Ibc * 0.01004 
    elif Arl == 3:
        valorArl = Ibc * 0.02436 
    elif Arl == 4:
        valorArl = Ibc * 0.0435
    elif Arl == 5:
        valorArl = Ibc * 0.0696
    print(salud + pension+ Ibc)
else:
    print(" ")
    print("-------")
    print(" ")
    print("Error")
    print("")
    print("-------")