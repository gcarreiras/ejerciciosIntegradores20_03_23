# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre = "", edad=0 , dni =0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad   

    def get_dni(self):
        return  self.dni    
    
    def set_dni(self, dni):
        self.dni = dni
    
    def mostrar(self):
        return self.nombre , self.dni ,  self.edad
    
    def es_mayor_de_edad(self):
        
        if self.edad > 18:
            return True
        return False
    
p1 = Persona("Gaston" , 36 , 00000000)
print (p1.mostrar())
print(p1.es_mayor_de_edad())
