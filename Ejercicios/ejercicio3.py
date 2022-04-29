#Crear un programa que pida una cantidad de segundos y que escriba cuantas horas, minutosy segundos son.
dato_de_usuario = input("Hola, regalame los segundos que quieras convertir ")
dato_de_usuario = int(dato_de_usuario)
horas = dato_de_usuario / 3600
minutos = dato_de_usuario / 60
print ("Los segundos convertidos a minutos son ")
print (minutos)
print ("Los segundos convertidos a horas son ")
print (horas)
print ("total de segundos ")
print (dato_de_usuario)