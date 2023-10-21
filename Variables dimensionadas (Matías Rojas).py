# 1. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente 
# forma: (nombre, dni, destino). Por ejemplo:
# *(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)+
# Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
# *(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)+
# Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
# - Agregar pasajeros a la lista de viajeros.
# - Agregar ciudades a la lista de ciudades.
# - Dado el DNI de un pasajero, ver a qué ciudad viaja.
# - Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
# - Dado el DNI de un pasajero, ver a qué país viaja.
# - Dado un país, mostrar cuántos pasajeros viajan a ese país.
# - Salir del programa.
def valid_dni(dni_input):
    if len(dni_input) == 7 or len(dni_input) == 8:
        return True
    return False

def add_passenger():
    passenger = []
    destiny_in_city = False
    print("------------------------------------")
    print("Ha seleccionado 'Agregar pasajeros a la lista de viajeros'")
    print("------------------------------------")
    name = input("Ingrese el nombre del pasajero: ").title()
    dni = ("")
    while valid_dni(dni) == False:
        dni = input("Ingrese el DNI del pasajero: ")
        if valid_dni(dni) == False:
            print("Ingrese un DNI válido")
    destiny = input("Ingrese el destino del pasajero (ciudad): ").title()
    for i in citys:
        for j in i:
            if destiny == j:
                destiny_in_city = True
    if destiny_in_city == False:
        print("Para agregar a un pasajero primero debe añadir la ciudad destino a la lista de ciudades")
        print("------------------------------------")
    else:
        passenger.append(name)
        passenger.append(dni)
        passenger.append(destiny)
        travelers.append(tuple(passenger))
        print("------------------------------------")

def add_city():
    city_country = []
    print("------------------------------------")
    print("Ha seleccionado 'Agregar ciudad a la lista de ciudades'")
    print("------------------------------------")
    city = input("Ingrese el nombre de la ciudad: ").title()
    country = input("Ingrese el nombre del país: ").title()
    city_country.append(city)
    city_country.append(country)
    citys.append(tuple(city_country))
    dict_citys[city] = country
    print("------------------------------------")

def consult_by_DNI():
    dni_in_travelers = False
    print("------------------------------------")
    print("Ha seleccionado 'Consultar país y ciudad por DNI'")
    print("------------------------------------")
    dni = input("Ingrese el DNI del cuál desea realizar la consulta: ")
    for i in range(len(travelers)):
        for j in range(len(travelers[i])):
            if travelers[i][j] == dni:
                print(f"El pasajero de DNI '{dni}' de nombre '{travelers[i][j-1]}' viajará a {travelers[i][j+1]} en {dict_citys[travelers[i][j+1]]}")
                dni_in_travelers = True
    if dni_in_travelers == False:
        print(f"No se encuentra registrado un pasajero con el DNI '{dni}'")
    print("------------------------------------")

def travelers_to_country():
    travelers_count = 0
    print("------------------------------------")
    print("Ha seleccionado 'Consultar cantidad de pasajeros que viajan a un país'")
    print("------------------------------------")
    country = input("Ingrese el país del que desea realizar la consulta: ").title()
    for value in dict_citys.values():
        if value == country:
            travelers_count += 1
    if travelers_count == 0:
        print("No hay pasajeros registrados que viajen a",country)
    if travelers_count == 1:
        print(f"{travelers_count} pasajero viajará a {country}")
    if travelers_count > 1:
        print(f"{travelers_count} pasajeros viajarán a {country}")
    print("------------------------------------")

def travelers_to_city():
    travelers_count = 0
    print("------------------------------------")
    print("Ha seleccionado 'Consultar cantidad de pasajeros que viajan a una ciudad'")
    print("------------------------------------")
    city = input("Ingrese la ciudad de la que desea realizar la consulta: ").title()
    for i in travelers:
        for citys in i:
            if citys == city:
                travelers_count += 1
    if travelers_count == 0:
        print("No hay pasajeros registrados que viajen a",city)
    if travelers_count == 1:
        print(f"{travelers_count} pasajero viajará a {city}")
    if travelers_count > 1:
        print(f"{travelers_count} pasajeros viajarán a {city}")
    print("------------------------------------")


travelers = []
citys = []
dict_citys = {}

option = -1
valid_option = [0,1,2,3,4,5]

print("Bienvenido!")
while option != 0:
    print("¿Qué desea hacer?:")
    print("1. Agregar pasajeros a la lista de viajeros")
    print("2. Agregar ciudades a la lista de ciudades")
    print("3. Consultar país y ciudad por DNI")
    print("4. Consultar cantidad de pasajeros que viajan a un país")
    print("5. Consultar cantidad de pasajeros que viajan a una ciudad")
    print("0. Salir")
    option = int(input())
    if option not in valid_option:
        print("------------------------------------")
        print("Ingrese una opción válida")
        print("------------------------------------")
        continue
    if option == 1:
        add_passenger()
    if option == 2:
        add_city()
    if option == 3:
        consult_by_DNI()
    if option == 4:
        travelers_to_country()
    if option == 5:
        travelers_to_city()
    if option == 0:
        print("------------------------------------")
        print("Hasta luego!")
        print("------------------------------------")
        break

# 2. Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual 
# contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
# *(‘Nuria Costa’, 5, 1234.5,’Calle 1 – 456’), (‘Jorge Russo’, 7, 3999, ‘Calle 2 – 741’)+
# Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y 
# retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente 
# puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que 
# contenga cada domicilio una sola vez.
def bills(original_sell_list):
    sell_dict = {}
    for i in range(len(original_sell_list)):
        customer = original_sell_list[i][0]
        customer_adress = original_sell_list[i][3]
        if customer not in sell_dict.keys():
            sell_dict[customer] = customer_adress
    return sell_dict

sells = [("Nuria Costa", 5, 1234.5,"Calle 1 – 456"), ("Jorge Russo", 7, 3999, "Calle 2 – 741"), ("Nuria Costa", 26, 5320,"Calle 1 – 456"), ("Alberto Torres", 2, 11000,"Calle 3 – 489"), ("Nuria Costa", 1, 7200.14,"Calle 1 – 456"), ("Alberto Torres", 17, 5135,"Calle 3 – 489"), ("Micaela Gonzalez", 11, 2352,"Calle 6 – 120")]
pending_customer_bills = bills(sells)
print("Las direcciones de los clientes a los cuales hay que entregarles factura de compra son:")
for i in pending_customer_bills.keys():
    print("-",pending_customer_bills[i])

# 3. Crear un programa para gestionar datos de los socios de un club, permitiendo:
# - Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar 
# son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar 
# con los datos de los socios fundadores ya cargados:
# o Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
# o Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
# o Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
# - Informar cantidad de socios del club.
# - Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
# - Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad 
# ingresaron el 14/03/2018.
# - Solicitar el nombre y apellido de un socio y darle de baja (eliminarlo del listado)
# - Imprimir el listado de socios completo.
partners = {
    1: {"Nombre": "Amanda Núñez", "Fecha ingreso": "17/03/2009", "Cuota al día": True},
    2: {"Nombre": "Bárbara Molina", "Fecha ingreso": "17/03/2009", "Cuota al día": True},
    3: {"Nombre": "Lautaro Campos", "Fecha ingreso": "17/03/2009", "Cuota al día": True}
}

def print_partners():
    print("Listado de socios: ")
    for num, data in partners.items():
        share = "al día" if data["Cuota al día"] else "Adeudada"
        print(f"Socio nro{num}, {data['Nombre']}, Ingresó: {data['Fecha ingreso']}, cuota {share}")
    print(f"Total de socios: {len(partners)}")

print_partners()

num_partner = int(input("Ingrese el número de socio que pagó todas las cuotas: "))
if num_partner in partners:
    partners[num_partner]["Cuota al día"] = True
    print(f"El socio nro{num_partner} ha pagado todas sus cuotas adeudadas")
else:
    print("El número de socio ingresado no es válido")


for num, data in partners.items():
    if data["Fecha ingreso"] == "13/03/2018":
        data["Fecha ingreso"] == "14/03/2018"

name = input("Ingrese el nombre y apellido del socio a dar de baja (Nombre Apellido): ")
partner_to_terminate = None
for num, data in partners.items():
    if data["Nombre"] == name:
        partner_to_terminate = num
        break

if partner_to_terminate is not None:
    del partners[partner_to_terminate]
    print(f"El socio {name} ha sido eliminado del sistema")
else:
    print("El socio no se encuentra en la lista")

print_partners()