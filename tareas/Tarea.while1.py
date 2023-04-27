num1 = 20
num2 = 20
resta=0
while num1 == num2 or num2 == num1:
    num1 = int (input("Digite un numero"))
    num2 = int (input ("Digite otro numero"))
    if num2 < num1:
        resta = num1 - num2
        print(f"El resultado de la resta es {resta}")
    else:
        resta = num2 - num1
        print(f"El resultado de la resta es: {resta}")
    while resta !=0:
        if num1 < num2:
            resta = resta - num1
            print(f"El resultado de la resta es: {resta}")
        else:
            resta = resta - num2
            print(f"El resultado de la resta es: {resta}")
        if resta <= 0:
            print("Ya no se puede restar mas: ")
            print("EL RESIDUO ES: ", resta)
            break
    