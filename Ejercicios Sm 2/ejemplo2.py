#if aninado

x = int(8)
'''
if 0<x:
    if x<10:
        print("x es un num positivo de 1 digito")

#alternativa a lo anterior
if 0<x and x <10:
    print("el dato x es un num de 1 digito.")       
'''

#condicional anidado con texto
curso = str("Python")
Curso = str("Ingles")
longitudTexto = len(curso)
if curso == "Python":
    if Curso == "Ingles":
        print("El alumno está matriculado en python e ingles")
else:
    print("El alumno no está matriculado en python")

if not curso:
    print("La variable curso está vacía.")    
else:
   print("La variable curso no está vacía, tiene una longitude caracteres ",longitudTexto)

#este siguiente condicional es similar al anterior pero usando funcion len almacenado en longitudTexto
if longitudTexto !=0:
    print("La variable curso no está vacía, tiene una longitude caracteres ",longitudTexto)
else:
   print("La variable curso está vacía.")    
 