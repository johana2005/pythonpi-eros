num = int(input ("digite un numero:"))

a = 10
b = 15
suma=0

for i in range (1,num):
     if num%i ==0:
        suma+=i


if suma == num:
    print (f"{num} Es un numero perfecto")
else :
    print(f"{num} No es un numero perfecto")