# 1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# •	mostrar(): Muestra los datos de la persona.
# •	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Person:
    def __init__(self, name=None, age=None, dni=None):
        self.__name = name
        self.__age = age
        self.__dni = dni

    def setName(self, new_value):
        if new_value != "" and new_value != " ":
            self.__name = new_value
        else:
            print("El nombre ingresado no es válido")
    def setAge(self, new_value):
        if new_value > 0 and new_value < 110:
            self.__age = new_value
        else:
            print("La edad ingresada no es válida")
    def setDni(self, new_value):
        if len(new_value) == 7 or len(new_value) == 8:
            self.__dni = new_value
        else:
            print("El DNI ingresado no es válido")

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getDni(self):
        return self.__dni

    def show(self):
        print("Nombre: ",self.__name)
        print("Edad: ",self.__age)
        print("DNI: ",self.__dni)

    def is_older_than_18(self):
        if self.__age >= 18:
            return True
        else:
            return False