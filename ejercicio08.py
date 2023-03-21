# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.

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
    


class Cuenta(Persona):
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        if self.cantidad < 0 :
            print("numeros en rojo")
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("necesario ingresar saldo positivo.......")

    def retirar(self, cantidad):
        ##if cantidad > 0 and cantidad <= self.cantidad:
          ## ¿permite numeros negativos si la cuenta esta en rojo......
            self.cantidad -= cantidad





class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    def es_titular_valido(self):
        return self.get_titular().get_edad() >= 18 and self.get_titular().get_edad() < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para realizar la retirada de dinero.")
    
    def mostrar(self):
        return "Cuenta Joven con bonificación del {}%".format(self.get_bonificacion())
    

p = Persona ("Gaston" , 36 , 00000000)
joven = CuentaJoven ( p , 50,  18)
print(joven.es_titular_valido())
print(joven.retirar(10))


p = Persona ("Toni" , 23 , 00000000)
joven = CuentaJoven ( p , 50,  18)
print(joven.es_titular_valido())
print(joven.retirar(10))
print(joven.mostrar())