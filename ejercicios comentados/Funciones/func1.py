# METODOS VS FUNCIONES
lista=[11,2,34,4,5] #lista
print(lista) #mostrar lista 
print(len(lista)) #organizar lista 
lista.sort()#agregar lista
print(lista) #mostrar lista con sus modificaciones 

#INTRODUCCION A LAS FUNCIONES CREADAS POR EL PROGRAMADOR

def saludo(receptor): # la funcion saludo tiene un atributo receptor
    print(f'Hola {receptor}') #mostrara hola mas lo que este en el receptor (es decir la funcion)

saludo('Aprendices')#las palabras que estan en la bariable 
saludo('soacha')
saludo('Sub director')

def saludar(receptor):
    return f'Hola {receptor}'

print(len(saludar('Aprendices'))) 
cadena=saludar('soacha')
print(cadena)
print(len(cadena)) #mostrara la cadena
cadena='Esto recibo de la funcion'+saludar('subdirector')
print(cadena) #mostrara la cadena, es decir, la frase mas la funcion 
#print(saludar('soacha'))
#print(saludar('Sub director'))