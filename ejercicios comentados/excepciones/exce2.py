value=0#la variable es igual a 0
try:#cuando queremos hacer una excepcion es necesario poner try
    value = int(input('Ingresa un número natural: '))#el input es para que digite y guarde el numero que va a poner 
    print('El recíproco de', value, 'es', 1/value)     #mostrara en la terminal el reciproco     
except ValueError: 
    print('No se que hacer con', value)    
except ZeroDivisionError: #cuando la divion es entre 0 y esto en python no se puede por eso sale este error 
    print('La división entre cero no está permitida en nuestro Universo.') #mostrara la frase 
print('continuacion.....')