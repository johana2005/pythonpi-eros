for i in range(11): # Es para hacer una comparacion pero cuando me estan dando un fin de comparacion, en este caso termina en 11
    if i%3==0: #Con este hacemos que i es se opere y con el "=="nos referimos a que de 0
        print(f'{i} es multiplo de 3') #muestra en pantalla la frase y el resultado que es la variable i
    else: # Esta es para dar la comparacion, es decir, lo opuesto 
        print(i) #mostrara en pantalla la variable "i"

for j in range(1,11):#Esta es otra forma de hacer una comparacion con for  la cual es ingresando el iicio y el final de la comparacion 
    print(j) #Mostara en pantalla los numeros del uno al diez 

for k in range(0,11,2): # Esta forma es para digitar el inicio, el final y la forma como va a saltar
    print(k) #mostrara en pantalla 

for i in range(20,0,-2):#Esta es una compacion igual que las anteriores solo que esta inicio, fin y se decrementa de a dos por el numero final del parentecis 
    print(i) #imprime en pantalla 