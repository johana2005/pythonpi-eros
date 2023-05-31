b={}
c={}

def fenc(tarea, clave, valor, diccionario):
    a=1
    diccionario.update({clave:valor})
    while True:
        a+=1
        clave = input("Escriba la clave: ")
        valor= input("Escriba un valor: ")
        diccionario.update({clave:valor})
        if a == tarea:
            break

    return diccionario

print(fenc(int(input("Escriba cuantas veces quiere llenar el diccionario: ")), input("Escriba la clave: "), input("Escriba el valor: "), b))



