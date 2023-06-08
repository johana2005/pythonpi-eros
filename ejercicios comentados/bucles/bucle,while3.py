n=int(input('ingrese numero')) #Se declara la variable n 
i=1 # Declaramos i 
while i<n: #comparamos si i es menor que n
    if i%7==0: #Esta es para realizar la comparacion
        print(f'{i} es multiplo de 7')
    else:
        print(i)
    i+=1