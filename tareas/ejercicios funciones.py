import random
a=0
mayor=0
menor=21
def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def mayorLista(lista):
    man=lista[0];
    for a in lista:
        if a > man:
            man=a
    return man

def menorLista(lista):
    menor=lista[0];
    for x in lista:
        if x < menor:
            menor=x
    return menor

def ordenar(lista):
    lista.sort()
    for lista in lista:
        print (lista)
        
def descender(lista):
    lista.sort(reverse=True)
    for lista in lista:
        print (lista)

from statistics import mode
def mediana (lista):
    media = len (lista) // 2
    lista.sort()
    if not len (lista) % 2:
        return (lista [media - 1] + lista[media]) / 2.0
    return lista[media]

l1=llenarLista(5,20)
print(l1)
print("La suma es: ", sumaLista(l1))
print("El promedio es: ", promedioLista(l1))
print("El mayor es: ", max(l1))
print("El menor es: ", min(l1))
print("El orden ascendente es: ", ordenar(l1))
print("El orden descendente es: ", descender(l1))
print("La  moda es: ", mode(l1))
print("La medana es: ", mediana(l1))
