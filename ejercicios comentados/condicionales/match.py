num1,num2=100,50 #pide dos numeros 
print('1-sumar') #los siguientes print aon para que el usuario elija la opcion que quiere que se desarrolle 
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')
op=int(input('que operacion?')) #un input para que pida el numero de la operacion que desea desarrollar 
match op: #con esta condicion podemos hacer que opere todas de una vez sin necesidad de poner diferentes for  
    case 1: #cada case es para que realize una operacion diferente 
        print(num1+num2)#esta es para sumar los dos numeros
    case 2:
        print(num1-num2)#restara los dos numeros
    case 3:
        print(num1*num2)#multiplicara los dos numeros 
    case 4:
        print(num1/num2)# //  / dividira los dos numeros 
    case 5:    
        print(num1%num2) #para sacar el mod de la operacion 
