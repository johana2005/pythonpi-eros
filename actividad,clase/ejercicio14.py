#Calcular todos los números de 3 cifras tales que la suma 
#de los cubos de las cifras es igual al valor del número.


#m= int(input("Digite un numero de 3 cifras : "))
for i in range(100, 111):
    num=i
    u = i % 10
    num=num//10

    d = num % 10
    
    k = d //10

    print(f"{k}  {d}   {f}")
   

