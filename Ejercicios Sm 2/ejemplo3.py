#dados 3 datos de entrada mostrar el mayor de ellos

a = int(input("Ingrese el 1er numero positivo: "))
b = int(input("Ingrese el 2do numero positivo: "))
c =int(input("Ingrese el 3er numero positivo: "))
if  a>c and a>b:
    print("El mayor es ",a)
elif b>a and b>c:
    print("El mayor es ",b)
else:
    print("El mayor es ",c)