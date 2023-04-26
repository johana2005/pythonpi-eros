largo= int (input("Digite el largo del rectangulo: "))
ancho= int (input( "digite la ancho del rectangulo:" ))
respuesta= (largo * ancho)
print ("El area de tu rectangulo es: ",respuesta)
i=2
for i in range (1, respuesta + 1):
    if i%2==0:
        print(f"El numero {i} es par")
    else:
        print (f"El numero {i} es impar") 
    


