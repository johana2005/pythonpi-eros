# num=1
# print(type(num))
# num="sena"
# print(type(num))
num=1 # son las variables 
cont=0
sum=0
menor=1000000
mayor=0
while num!=0: #para realizar la comparacion
    num=int(input('ingrese numero'))
    cont=cont+1  #Un contador es para que se sumen los valores constantes  
    sum=sum+num #se suman los numeros 
    if num>mayor: # numero es mayor que, con la variable mayor
        mayor=num
    if num<menor and num!=0: # hace la compracion con and que es como y para poner dos opciones 
        menor=num

print(f'fueron ingresados {cont-1} numeros') # va a mostrar cada uno, dependiendo lo que quiere dar a entender  
print(f'La suma es {sum}')
print(f'El promedio es {sum/(cont-1)}')
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')