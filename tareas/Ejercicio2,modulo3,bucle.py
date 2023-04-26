# confirmar un inicio de cecion

identificacion = (input("Escriba su tipo de documento"))
numIdent = (input(" Escriba su numero de documento"))
confdocument= (input("Confirma tu numero de documento"))
contraseña =(input("Digite la contraseña"))
confcont = (input("confirme su contraseña"))

if numIdent == confdocument:
    print("Estas en el sistema")
while confdocument != numIdent:
    print ("Intento fallido")
    confdocument = int (input("Confirma tu numero de documento"))
    