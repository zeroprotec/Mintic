#ingresa un valor 
texto = str(input("Ingresa una palabra "))
# se crea un ciclo for 
for i in texto:
    print(i)
for indice in range(len(texto)):
    caracter = texto[indice]
    print("En el indice {} tenemos a '{}'".format(indice, caracter))