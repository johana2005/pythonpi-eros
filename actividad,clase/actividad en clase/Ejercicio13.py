num=int (input("Digite un numero de 4 cifras: "))
a4= num % 10
a3= int ((num % 100) / 10)
a2= int ((num % 1000) / 100)
a1= int ((num - (num % 1000)) / 1000)
print (str(a4)+str(a3)+str(a2)+str(a1))
