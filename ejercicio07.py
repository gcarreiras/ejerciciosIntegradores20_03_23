# . Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.



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
    


class Cuenta:
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


p = Persona ("Gaston" , 36 , 00000000)
c1 = Cuenta( p, 45.5)

print(p.get_nombre())

print(c1.retirar(60))
print(c1.get_cantidad())