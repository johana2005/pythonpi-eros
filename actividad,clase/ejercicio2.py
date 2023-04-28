n =  int (input("Ingrese un numero entero positivo :"))
if n > 1:
    for i in range (2, n):
      if (n%i) == 0:
         print(n,"No es un numero primo")
         break 
      else:
         print(n,"Es numero primo")
else:
   print(n,"No es un numero primo")
   