# 2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y 
# cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# •	mostrar(): Muestra los datos de la cuenta.
# •	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# •	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
class Account:
    def __init__(self, holder, amount=0):
        self.__holder = holder
        self.__amount = amount
    
    def __setHolder(self, new_value):
        self.__holder = new_value
    def __setAmount(self, new_value):
        self.__amount = new_value
    def getHolder(self):
        return self.__holder
    def getAmount(self):
        return self.__amount

    def show_account_details(self):
        print("Datos de la cuenta: ")
        print("Nombre: ", self.__holder)
        print("Dinero: $", self.__amount)

    def deposit(self, money_amount):
        self.__amount += money_amount
    def withdraw(self, money_amount):
        self.__amount -= money_amount