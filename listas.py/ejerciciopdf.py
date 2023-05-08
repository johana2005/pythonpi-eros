import random
lista=[]
lista1=[]
sum=0
sum1=0
may=0
may1=0
men=0
men1=0
pares=0
impares=0
cont1=0
coni=0
c=0
b=0

for i in range (10):
    n=random.randint(10,15)
    lista.append(n)
print (lista)

for i in range (10):
    n1=random.randint(10,15)
    lista1.append(n1)
print (lista1)

for m in lista:
    sum=sum + m
    if m % 2 == 0:
        pares+=1
        
    if c > may :
            may = c
    if c < men :
            men=c
else:
        impares+=1
prome=sum/len(lista)    

for h in lista1:
    sum1=sum1 + h
    if h % 2 ==0:
        cont1+=1
    if  b > may1 :
            may1= b
    if b < men1:
            men1=b
else:
        coni+=1
prome1= sum1 /len(lista1)

if cont1 > pares:
    print (f"La lista dos tiene mayor cantidad de pares {cont1} y la lista uno tiene estos {pares} impares")
elif cont1 < pares:
    print (f"La lista uno tiene mas pares {pares} y la lista dos tiene {cont1}")
else:
    print("Las dos listas tienen los mismos pares")
if coni > impares:
    print(f"La lista dos tiene mas impares {coni} y la uno tiene {impares}")
elif coni < impares:
    print (f"La lista uno tiene mas impares {impares} y la dos tiene {coni}")
else:
    print("Las dos tienen la misma cantidad de imparaes ")
if sum > sum1:
    print(f"la suma mayor es la lista uno y la suma es: {sum}")
else:
    print(f"La suma mayor es la lista dos y la suma es: {sum1}")
if may > may1:
    print(f"El numero mayor entre las dos listas es: {may}")
elif may < may1:
    print(f"El numero mayor de las dos listas es: {may1}")
else:
    print("Las dos listas tiene el mismo numero mayor")
if men > men1:
    print(f"El numero menor entre las dos listas es: {men1}")
elif men < men1:
    print(f"El numero menor entre las dos listaas es: {men}")
else:
    print("Las dos listas tienen el mismo numero menor")

    print(prome,prome1)
    prome_conj =(prome + prome1) / 2
    print (f"El promedio entre las dos listas es: {prome_conj}")

if prome < prome_conj:
    print("El promedio de la lista uno esta por encima del promedio conjunto ")
elif prome > prome_conj:
     print("El promedio de la lista uno esta por encima del primedio")
else:
     print("El promedio de las listas son iguales ")
if prome1 < prome_conj:
     print("El promedio de la lista dos esta por debajo del promedio ")
elif prome1 > prome_conj:
     print("El promedio de la lista dos esta por encima del promedio ")
else: 
     print ("El promedio de la lista dos es igual ")