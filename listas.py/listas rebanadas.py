import random
tam=random.randrange(20,30)
#lista=[random.randrange(0,5)for i in range(tam)]
o=0
promedio=0
suma=0
calificacion=[round(random.random()*5,1)for i in range(tam)]
print(calificacion)
for p in range(tam):
  for m in range(p+1,tam):
    if calificacion[p] > calificacion[m]:
        lol=calificacion[p]
        calificacion[p]=calificacion[m]
        calificacion[m]=lol
print (calificacion)
#lista=["aprobo" if x >= 3.0 else "reprobo" for x in calificacion]
#print (lista)
aprobo=[p for p in calificacion if p >= 3.0]
print(f"aprobo {aprobo}")
reprobo=[m for m in calificacion if m < 3.0]
print(f"reprobo {reprobo}")
lista1=["Decepcionante" if o<=1.0 else "pesimo" for o in calificacion]
Decepcionante=[o for o in calificacion if o<=1.0]
print(f"Decepcionante {Decepcionante}")
pesimo=[o for o in calificacion if o>1.0 and o<=2.0]
print(f"pesimo: {pesimo}")
lista2=["Mediocre"if o<3.0 else "Bueno" for o in calificacion]
Mediocre=[o for o in calificacion if o>2.0 and o<=3.0]
print(f"Mediocre: {Mediocre}")
bueno=[o for o in calificacion if o>3.0 and o<=4.0]
print(f"Bueno: {bueno}")
superior=[o for o in calificacion if o>4.0 and o<=5.0]
print(f"Superior: {superior}")
for n in aprobo:
   suma= suma + n
print ("La suma de los aprobados es: ",suma)
promedio= suma / len(aprobo)
print("El promedio de los reprobados es: ",promedio)
for f in reprobo:
   suma= suma + f
print("La suma de los reprobados es: ",suma)
promedio= suma / len(reprobo)
print("El promedio de los reprobados es: ", promedio)