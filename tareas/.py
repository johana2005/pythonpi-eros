num1,num2=100,50  # Declara las variables numeros los cuales son dos 
print('1-sumar')   # Imprime todas las operaciones segun el numero que digiten  
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')
op=int(input('que operacion?')) # pregunta la operacion que desea realizar 
match op: #evaluar condiciones 
    case 1: 
        print(num1+num2) # Imprimir en pantalla las operaciones  
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)# //  /
    case 5:    
        print(num1%num2)