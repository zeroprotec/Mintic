def materias(materia1,materia2,materia3,materia4,materia5):
    totalmaterias = (materia1,materia2,materia3,materia4,materia5)
    return totalmaterias
def materias(cadena):
    asignaturas=cadena.split(",")
    return asignaturas


def multiplicarNumeros(numeros):
    producto = 1
    for n in numeros:
        producto *= n
    return producto

def listaFrutas(lista):
    for fruta in lista:
        print(fruta)

print(materias(mat,ing,soci,))