cont =0
for n in range (2,1001):
    primo =1
    for i in range (2,int (n ** 0.5)+1):
        if n%i == 0:
            primo =0
    if primo:
        cont +=1
        print (n)
print (f"Hay {cont} numeros primos")