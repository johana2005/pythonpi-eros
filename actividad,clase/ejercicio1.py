num1 = int (input("Digite el numero que desea sacar los divisoles "))
resultado = 1
i = 0
for i in range (1, num1 +1 ):
  if num1 % i == 0:
    print (i)
