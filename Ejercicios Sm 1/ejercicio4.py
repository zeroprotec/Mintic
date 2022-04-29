# escribe un programa que pida el peso en kg y la altura en mts de una persona

peso_usuario = input("Hola, regalame tu peso ")
peso_usuario = int(peso_usuario)
altura_usuario = input("Hola, regalame tu altura ")
altura_usuario = float(altura_usuario)
imc = peso_usuario / (altura_usuario)**2
imc = str(imc)
print("Hola este es su indice de masa corporal " + imc)