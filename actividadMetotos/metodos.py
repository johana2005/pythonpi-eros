class Empleado:
    def _init_(self, nombre, cargo,horas, salario,incremento):
        self.__nombre= nombre
        self.__cargo= cargo
        self.__horas=horas
        self.__salario= salario
        self.__incremento= incremento
        

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre=nombre
    
    def getCargo(self):
        return self.__cargo
    def setCargo(self, cargo):
        self.__cargo=cargo
    
    def getHoras(self):
        return self.__horas
    def setHoras(self, horas):
        if horas <= 40:
            x=horas*4833
            self._salario= self._salario+ x
        else:
            return self.__salario
    
    def getSalario(self):
        return self.__salario
    def setSalario(self, salario):
        self.__salario= salario
        
    def getIncremento(self):
        return self.__incremento
    def setIncremento(self, incremento):
        self.__incremento= incremento
        if self.__salario >= 1160000:
            self.__salario + 0.1612 
        else:
            self.__salario + 0.1312
            return self.__incremento
                    
p=Empleado ("michell", "Ingenieria",10 , 1160000, 1160000)
print(p.getNombre())
print(p.getCargo())
print(p.getHoras())
print(p.getSalario())
print(p.getIncremento())