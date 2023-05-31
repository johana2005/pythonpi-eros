españolIngles={}
inglesEspañol={}

def spen(reps, clave, valor, diccionario):
    c=1
    diccionario.update({clave:valor})
    while True:
        c+=1
        clave = input("Escriba la clave: ")
        valor= input("Escriba un valor: ")
        diccionario.update({clave:valor})
        if c == reps:
            break

    return diccionario

print(spen(int(input("Escriba cuantas veces quiere llenar el diccionario: ")), input("Escriba la clave: "), input("Escriba el valor: "), españolIngles))

