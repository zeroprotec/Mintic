#se utiliza el and para unnir dos condiciones a evaluar.

x = int (input("Ingrese un numero "))
if 0 < x and x < 10:
    print("x es un numero positivo de un solo digito.")
# Alternativa al codigo anterior
if 0 < x < 10:
    print("x es un numero positivo de un solo digito.")