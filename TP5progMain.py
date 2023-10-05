from TP5progFunc import id_club, is_multiple_of, average_temperature, extra_space, min_max_num, area_perimeter_circumference, login, list_reciever, is_prime_num, factorial, digit_in_number, digit_sum


# 3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
# Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento 
# mediante el ingreso de un nombre vacio.
# Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, 
# en cuyo caso será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario 
# en un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad 
# de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
# Nombre: María Ines Rosales
# DNI: 25469648
# ID -> Maria7254
name_lastname = input("Ingrese su nombre completo (Ingrese hasta dos nombres y un apellido): ")
name_lastname = name_lastname.title()
name_lastname_aux = name_lastname
dni = input("Ingrese su DNI: ")
while len(dni) != 7 and len(dni) != 8:
    dni = input("El DNI ingresado no es válido, intentelo de nuevo: ")
id_club_associate = id_club(name_lastname, dni)
print("Sus datos son los siguientes: ")
print(f"Nombre: {name_lastname_aux}")
print(f"DNI: {dni}")
print(f"ID: {id_club_associate}")

# 4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
num = input("Ingrese un número: ")
multiple = input("Ingrese un múltiplo del número "+num+": ")
if is_multiple_of(int(num), int(multiple)):
    print("El número "+multiple+" es múltiplo de "+num)
else:
    print("El número "+multiple+" no es múltiplo de "+num)

# 5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de 
# cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
days = int(input("Ingrese la cantidad de días de los que ingresará la temperatura: "))
counter = 1
while counter <= days:
    print("Día ",counter,"-")
    min_temperature = float(input("Ingrese la temperatura mínima: "))
    max_temperature = float(input("Ingrese la temperatura máxima: "))
    print(f"La temperatura media del día {counter} es: {average_temperature(min_temperature,max_temperature)}°")
    counter += 1

# 6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio 
# adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa 
# principal donde se use dicha función.
text = input("Ingrese un texto: ")
print("El texto ingresado procesado es: "+extra_space(text))

# 7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
nums = []
num = input("Ingrese un número: ")
nums.append(int(num))
while num != "s":
    num = input("Ingrese otro número, para finalizar ingrese 's': ")
    if num == "s" or num == "S":
        break
    nums.append(int(num))
num_max, num_min = min_max_num(nums)
print(f"El número máximo de la lista es {num_max} y el número mínimo es {num_min}")

# 8.	Diseñar una función que calcule el área y el perímetro de una circunferencia. 
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
radius = float(input("Ingrese el radio de la circunferencia: "))
area_c, perimeter_c = area_perimeter_circumference(radius)
print(f"El área de la circunferencia es: {area_c:.2f}")
print(f"El perímetro de la circunferencia es: {perimeter_c:.2f}")

# 9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te 
# devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe 
# el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
# solamente tenemos tres oportunidades para intentarlo.
logintry = 3
valid = False
print("Bienvenido al sistema")
print("Inicie sesión:")
while logintry != 0 or valid != True:
    if logintry == 0:
        break
    user = input("Nombre de usuario: ")
    passw = input("Contraseña: ")
    valid,logintry = login(user, passw, logintry)
    if valid:
        print("Ha iniciado sesion correctamente")
        break
    else:
        if logintry == 1:
            print(f"El nombre o la contraseña son incorrectos. le queda {logintry} intento")
        else:
            print(f"El nombre o la contraseña son incorrectos. le quedan {logintry} intentos")

# 11.	Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado 
# de aplicar la función dada a cada uno de los elementos de la lista.
user_list = []
user_input = ""
while user_input != "salir":
    user_input = input("Ingrese un elemento de la lista: ")
    if user_input.lower() == "salir":
        break
    if user_input.capitalize() == "True" or user_input.capitalize() == "False":
        user_input = bool(user_input)
    else:
        try:
            user_input = int(user_input)
        except:
            try: 
                user_input = float(user_input)
            except:
                    pass
    user_list.append(user_input)
user_list = list_reciever(user_list)
print("La lista ingresada ha sido modificada: ")
print(user_list)

# 14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función 
# booleana que lo decida.
num = int(input("Ingrese un número entero: "))
prime_num = is_prime_num(num)
if prime_num:
    print("El número ingresado es primo")
else:
    print("El número ingresado no es primo")

# 15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la 
# cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.
num = ""
amount_num = 0
while num != "salir":
    num = input("Ingrese un número (para finalizar ingresa 'salir'): ")
    if num.lower() == "salir":
        break
    try:
        num = int(num)
        if num >= 0:
            print(f"El factorial de {num} es: ", factorial(num))
        else: 
            factorial(num)
        amount_num += 1
    except:
        print("Ingrese un número")
print("La cantidad de números leídos es: ",amount_num)

# 16.	Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito 
# en el número, utilizando para ello una función que calcule la frecuencia.
num = " "
while num != "":
    num = input("Ingrese un número entero: ")
    digit = input("Ingrese el dígito que desea buscar en el número ingresado: ")
    try: 
        num = int(num)
        digit = int(digit)
        break
    except:
        print("Ingrese solo números enteros")
num = str(num)
digit = str(digit)
frecuency = digit_in_number(num, digit)
print(f"El digito '{digit}' se repite {frecuency} veces en el número '{num}'")

# 17.	Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que 
# no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e 
# informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el 
# factorial del mayor número ingresado.
biggest_num = 0
num = ""
while num != " ":
    num = input("Ingrese un número primo (para finalizar ingrese un número no primo): ")
    if is_prime_num(int(num)) != False:
        digit = input("Ingrese el dígito que desea buscar en el número ingresado: ")
        print(f"La suma de los dígitos del número {num} es: {digit_sum(num)}")
        print(f"El digito '{digit}' se repite {digit_in_number(num, digit)} veces en el número '{num}'")
        if int(num) > biggest_num:
            biggest_num = int(num)
    else:
        break
print(biggest_num)
print(f"El factorial del mayor número ingresado ({biggest_num}) es: {factorial(biggest_num)}")
# reutilizo las funciones:
# digit_in_number
# factorial
# is_prime_num
