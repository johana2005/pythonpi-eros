import random # el ramdom genenra numeros aleatorios 
lista=[] #Esta creando una lista basia 
cuadrado=[] #esta creando la segunda variable de igual forma basia  
tam=random.randint(5,10) # va a crear un numero aleatorio entre 5 y 10
print(tam) #mostrara en pantalla el numero 
for i in range(tam): #va a realizar una comparacion
    num=random.randrange(100) # dentro del rango de 100 
    lista.append(num)# van a en listar num
print(lista) #muestre en pantalla la lista 

for i in range(len(lista)): 
    cuadrado.append(lista[i]*2)# vamos a sacar el uadrado 
    #lista[i]=lista[i]**2
   # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado) #mostramos el resultado del cuadrado
print(sum(lista))# mostramos la sumatoria 