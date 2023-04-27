x,y=3,5 # Esta declarando las variables con numeros 
cont=1 # un contador para hacer la suma de un valor constante  
while not(x%y==0 or y%x==0):# Hace una comparacion con not para que sea lo opuesto
    print(f'intento numero {cont}') #muestra en pantalla el la frase y el contador 
    x=int(input('ingrese numero')) #pide en pantalla el numero x
    y=int(input('ingrese numero'))#pide en pantalla el numero Y
    cont+=1 #Le suma uno

print(f'{x} y {y} son factor') #muestra si es factor o no 