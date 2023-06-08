#Tip para solucionar numeral 14
u,d,c=0,0,0 #declaramos tres variables que son iguales a 0
for i in range(100,1000): #creara un numero aleatorio 
    #256
    num=i #es una variable que declara que i es igual a num
    u=num%10 #so diferentes operaciones 
    num=num//10
    d=num%10
    c=num//10
    #print(f'{u}  {d}  {c}')
    cubo=(u**3)+(d**3)+(c**3)   #en esta linea va a realizar la operacion 
    #print(f'cubo {cubo}')
    #print(f'num {num}')
    if cubo==i:
        print(i) #esto mostrara en la terminar la i 