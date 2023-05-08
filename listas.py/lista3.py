import random
lista=[]
n=int (input("Escriba el numero "))
num1=0
num2=1
sol=0
for m in range (n):
    sol=num1+num2
    lista.append(sol)
    num1=num2
    num2=sol
print (lista)