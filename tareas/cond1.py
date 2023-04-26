x=int(input('ingrese numero')) # Declara las tres variables, como entero y deja que ingrese el numero 
y=int(input('ingrese numero'))
z=int(input('ingrese numero'))
#indentación
if x>y:      #hace la comparacion con mayor que 
    if x>z:      #comparea lo opuesto 
        print(f'el mayor es {x}')   # Imprime en pantalla si el mayor es x
    else: # hace la comparacion 
        print(f'el mayor es {z}') # Inprime en pantalla si el mayor es Z
else:   
    if y>z:
        print(f'el mayor es {y}')  # inprime en pantalla si el mayor es y
    else:
        print(f'el mayor es {z}') #inprime en pantalla si el mayor es z