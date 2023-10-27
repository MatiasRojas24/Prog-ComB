"""# 1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# •	mostrar(): Muestra los datos de la persona.
# •	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
from Person import Person
persona1 = Person()
persona1.setName(input("Ingrese el nombre de la persona: "))
persona1.setAge(int(input("Ingrese la edad de la persona: ")))
persona1.setDni(input("Ingrese el DNI de la persona: "))
print()
persona1.show()
if persona1.is_older_than_18():
    print(persona1.getName(), "es mayor de edad")
else:
    print(persona1.getName(), "no es mayor de edad")
print("")

# 2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y 
# cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# •	mostrar(): Muestra los datos de la cuenta.
# •	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# •	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
from Account import Account
Account1 = Account(
    holder= "Matías Rojas",
    amount= 100000
)
Account1.show_account_details()
Account1.withdraw(int(input("Ingrese la cantidad de dinero que desea retirar: $")))
Account1.show_account_details()
Account1.deposit(int(input("Ingrese la cantidad de dinero que desea ingresar: $")))
Account1.show_account_details()
print("")

# 3.	Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para 
# inicializar los atributos, imprimir el valor del lado con un tamaño mayor y
# el tipo de triángulo que es (equilátero, isósceles o escaleno).
from Triangle import Triangle
triangle1 = Triangle(
    side_a=7,
    side_b=7,
    side_c=7
)
triangle2 = Triangle(
    side_a=6.14,
    side_b=6.14,
    side_c=9.39
)
triangle3 = Triangle(
    side_a=11,
    side_b=8.41,
    side_c=1.314
)
print("Triángulo 1:")
print("Tipo de triángulo:",triangle1.triangle_type())
print("Lado más largo:",triangle1.larger_side())
print("")
print("Triángulo 2")
print("Tipo de triángulo:",triangle2.triangle_type())
print("Lado más largo:",triangle2.larger_side())
print("")
print("Triángulo 3:")
print("Tipo de triángulo:",triangle3.triangle_type())
print("Lado más largo:",triangle3.larger_side())
print("")"""

# 4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
# Además deberá mostrar un menú con las siguientes opciones:
# •	Añadir contacto
# •	Lista de contactos
# •	Buscar contacto
# •	Editar contacto
# •	Cerrar agenda
from Agenda import Agenda
contacts = []
option = 1

print("Bienvenido")
while option != 0:
    print("¿Qué desea hacer?")
    print("1. Añadir contacto")
    print("2. Ver lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("0. Cerrar agenda")
    option = int(input())
    print()
    if option == 1:
        name_input = input("Ingrese el nombre del contacto: ").title()
        phone_input = input("Ingrese el número de teléfono del contacto: ")
        email_input = input("Ingrese el email del contacto: ")
        print()
        new_contact = Agenda(
            name= name_input,
            phone= phone_input,
            email= email_input
        )
        contacts.append(new_contact)
    if option == 2:
        for i in range(0,len(contacts)):
            print(f"Contacto {i+1}:")
            print(contacts[i].showContact())
            print()
    if option == 3:
        search_name = input("Ingrese el nombre del contacto que desea buscar: ").title()
        print()
        registred_contact = False
        for i in range(0, len(contacts)):
            if contacts[i].getName() == search_name:
                registred_contact = True
                contact_found_pos = i
        if registred_contact:
            print("Se ha encontrado al contacto de nombre",search_name,"la información del contacto es la siguiente: ")
            print(contacts[contact_found_pos].showContact())
            print()
        else:
            print("No se ha encontrado al contacto en la agenda")
            print()
    if option == 4:
        pos = int(input("Ingrese el número del contacto que desea editar (posición): "))-1
        new_name= input("Ingrese el nuevo nombre del contacto: ").title()
        new_phone= input("Ingrese el nuevo número telefónico del contacto: ")
        new_email= input("Ingrese el nuevo email del contacto: ")
        print()
        contacts[i].setName(new_name)
        contacts[i].setPhone(new_phone)
        contacts[i].setEmail(new_email)
        print("Se ha editado el contacto")
        print()
    if option == 0:
        print("Hasta luego!")