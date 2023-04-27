num1 = int(input("Escriba un numero: "))
num2 = int(input("Escriba otro numero: "))
resta = 0
if num2 < num1:
    resta = num1 - num2
    print("El resultado de la resta es:" , resta)
else:
    resta = num2 - num1
    print("El resultado de la resta es:", resta)


while resta !=0:
    if num1 < num2:
        resta = resta - num1
        print("El resultado de la resta es:" , resta)
    else:
        resta = resta - num2
        print("El resultado de la resta es: ", resta)
    if resta <= 0:
        print("Ya no se puede restar mas. ")
        print("EL RESIDUO ES: ", resta)
        break
    