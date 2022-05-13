# texto
s = str(input("Ingresa una palabra "))
# letra a encontrar
c = str(input("Ingresa la letra a buscar en la palabra "))
cont = 0
# ciclo for
for i in range(len(s)):
    letra = s[i]

    if(letra == c):
        cont = 1+cont
        print("En el indice {} tenemos a '{}'".format(i, letra))
print("La letra ",c,"se encuentra en la frase",s,cont,"veces")