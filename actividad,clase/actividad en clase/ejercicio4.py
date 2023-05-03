numero = int(input("Ingrese un numero: "))
for i in range (2, numero+1):
    n=0
    for h in range (1, (i//2)+1):
        if ((i%h)==0):
            n = n + h
    if (n==i):
        print ("%5 Es perfecto" %i)
    else: 
        print ("%5 no es perfecto" %i)