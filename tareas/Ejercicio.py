i=0

sumapares = 0
sumainpares = 0

for i in range (1, 100 +1):
    if i % 2 == 0:
        sumapares+=i 
    else:
        sumainpares+=i

print (f"La suma de los pares es:{sumapares}")
print (f"La suma de los numeros impsres es: {sumainpares}")
