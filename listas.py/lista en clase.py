import random
lista=[]
cuadrado=[]
mayor=0
menor=101
sum=0
tam= random.randint(10,20)
print(tam)

for i in range (tam):
    num=random.randrange(100)
    lista.append(num)
    sum += num
    j=num
    if j > mayor:
       mayor=j
    if j< menor:
       menor=j   
    prom=sum/tam
    
print(lista)
print(sum)
print(prom)
print (f"su numero mayor es:{mayor}  y  su numero menor es: {menor}")
print ()

lista.sort()
if tam % 2 !=0:
   m=(tam//2)
   print("la mediana es ",lista[m])
else:
   m=(tam//2)
   m=(lista[m-1])+(lista[m])
   m/=2
   print(f"la mediana es: {m}")

   