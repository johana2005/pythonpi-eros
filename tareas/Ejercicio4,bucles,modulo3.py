# Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atreas desde ese numero hasta cero separados por comas

numero = int (input("Escriba un numero entero positivo "))

i = 0
for i in range (numero, 0, -1):
    numero -= 1
    
    print (numero )