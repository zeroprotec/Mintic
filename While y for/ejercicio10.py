peso = (int())
def peso_a_euro(peso):
    return peso / 4500

print(peso_a_euro(10000))
    

    
def procesar_dato(peso,volumen):
    if peso < 2 and volumen < 0.027:
        return True
    else:
        return False
    
print(procesar_dato(3,2))

def par_impar(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False
    
print(par_impar(24))