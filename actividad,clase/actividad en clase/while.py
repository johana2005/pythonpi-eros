num =1 
print ("cuantas edades promediara")
prom = 0
cant = int (input())

while num<= cant:
    print(f"Ingrese la edad: {num}")
    edad = float(input())
    prom+=edad 
    num+=1
print ("El promedio de edades es:", prom/cant)
