value=0 #la variable es igual a 0
try: #cuando queremos hacer una excepcion es necesario poner try
    value = int(input('Ingresa un número natural: ')) #el input es para que digite y guarde el numero que va a poner 
    print('El recíproco de', value, 'es', 1/value)        #mostrara en la terminal el reciproco
except: #con este se prevee que salga algun error y en cambio aparezca la frese que se pone por defecto 
    print('Debio ingresar un numero') #si sucede la excepcion mostrara esta frase en pantalla 

print('el programa continua')#si no pasa la excepcion mostrara esta frase en pantalla 