# 1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola 
# que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.
a_comp = int(input("Ingrese cuantos años tiene su computadora: "))
if a_comp <= 2 and a_comp >= 0: 
    print("El computador es nuevo.")
if a_comp > 2:
    print("El computador es viejo")

# 2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
if a_comp < 0:
    print("El número ingresado no es válido.")

# 3- Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación. 
# Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.
nombres = input("Ingrese dos nombres [nombre1, nombre2]: ")
nombre_1 = nombres[0:nombres.find(",")]
nombre_2 = nombres[nombres.find(" ")+1:]
if nombre_1[0] == nombre_2[0]:
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

# 4-Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, 
# candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B o C) se debe imprimir el mensaje: 
# ‘Usted ha votado por el partido [color del candidato elegido]. Si el usuario ingresa una opción que no corresponde a 
# ninguno de los candidatos disponibles, indicar ‘Opción errónea.’
print("Ingrese 1, 2 o 3 para votar a su candidato")
print("1 - Partido Rojo")
print("2- Partido Verde")
print("3- Partido Azul")
voto = int(input())
if voto == 1:
    print("Usted ha votado al partido Rojo")
elif voto == 2:
    print("Usted ha votado al partido Verde")
elif voto == 3:
    print("Usted ha votado al partido Azul")
else:
    print(f"'{voto}' no es una opción válida.")

# 5-Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
# Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
# informarle que no se puede procesar el dato.
letra = input("Ingrese una letra: ")
letra = letra.lower()
if len(letra) > 1:
    print("Solo debe ingresar una letra")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Es una vocal")

# 6-Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible 
# por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
year = int(input("Ingrese un año: "))
if year%100 == 0 and year%400 == 0:
    if year%4 == 0:
        print(f"El año {year} es bisiesto")
elif year%4 == 0 and year%100 != 0:
    print(f"El año {year} es bisiesto")

# 7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
nums = input("Ingrese tres números [x, y, z]: ")
nums = nums.split()
num1 = nums[0]
num2 = nums[1]
num3 = float(nums[2])
num1 = float(num1[0:num1.find(",")])
num2 = float(num2[0:num2.find(",")])
menor = num1
if menor > num2:
    menor = num2
if menor > num3:
    menor = num3
print("El menor, de los tres números ingresados, es: ", menor)

# 8- Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y 
# la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. 
# Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
usuario = input("Ingrese su nombre de usuario: ")
contr = input("Ingrese su contraseña: ")
if usuario == "Gwenvere":
    if contr == "excalibur":
        print("Usuario y contraseña correctos. Puede ingresar a Camelot")
    else:
        print("Acceso denegado")
else:
    print("Acceso denegado")

# 9- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior 
# a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por 
# pantalla el grupo que le corresponde.
nombre = input("Ingrese su nombre: ")
nombre = nombre.lower()
genero = input("Ingrese su genero [M/F]: ")
genero = genero.lower()
if nombre[0] == "a" or nombre[0] == "b" or nombre[0] == "c" or nombre[0] == "d" or nombre[0] == "e" or nombre[0] == "f" or nombre[0] == "g" or nombre[0] == "h" or nombre[0] == "i" or nombre[0] == "j" or nombre[0] == "k" or nombre[0] == "l" or nombre[0] == "m":
    if genero == "f":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")
if nombre[0] == "n" or nombre[0] == "o" or nombre[0] == "p" or nombre[0] == "q" or nombre[0] == "r" or nombre[0] == "s" or nombre[0] == "t" or nombre[0] == "u" or nombre[0] == "v" or nombre[0] == "w" or nombre[0] == "x" or nombre[0] == "y" or nombre[0] == "z":
    if genero == "m":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")

# 10- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de 
# forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la 
# edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene 
# entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.
edad_cl = int(input("Ingrese la edad del cliente: "))
if edad_cl < 4:
    print("Puede ingresar sin costo")
if edad_cl >= 4 and edad_cl < 18:
    print("El costo de ingreso es de $500")
if edad_cl >= 18:
    print("El costo de ingreso es de $1000")

# 11- La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para 
# cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta 
# le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de 
# la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es 
# vegetariana o no y todos los ingredientes que lleva.
menu = input("Indique si desea un menu vegetariano o no [S/N]: ")
menu = menu.lower()
if menu == "s":
    print("Los ingredientes del menu vegetariano son los siguientes: ")
    print("(Todas las pizzas vienen con mozarella y tomate)")
    print("- Pimiento")
    print("- Tofu")
    ingrediente_v = input("Elija UN ingrediente: ")
    ingrediente_v = ingrediente_v.lower()
    if ingrediente_v == "pimiento" or ingrediente_v == "tofu":
        print("Su orden es la siguiente: ")
        print(f"Pizza vegetariana con mozarrella, tomate y {ingrediente_v}")
    else:
        print("Su pedido no es válido")
if menu == "n":
    print("Los ingredientes del menu vegetariano son los siguientes: ")
    print("(Todas las pizzas vienen con mozarella y tomate)")
    print("- Peperoni")
    print("- Salmón")
    print("- Jamón")
    ingrediente_nv = input("Elija UN ingrediente: ")
    ingrediente_nv = ingrediente_nv.lower()
    if ingrediente_nv == "peperoni" or ingrediente_nv == "salmón" or ingrediente_nv == "jamón":
        print("Su orden es la siguiente: ")
        print(f"Pizza con mozarrella, tomate y {ingrediente_nv}")
    else:
        print("Su pedido no es válido")

# 12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado 
# desde ese año o cuántos años faltan para llegar a ese año.
years = input("Ingrese el año actual y un año cualquiera [año_actual, año_x]: ")
an_actual = int(years[0:years.find(",")])
an_x = int(years[years.find(" ")+1:])
if an_actual > an_x:
    pas = an_actual - an_x
    print(f"Han pasado {pas} años desde el año {an_x}.")
if an_actual < an_x:
    falt = an_x - an_actual 
    print(f"Faltan {falt} años para el año {an_x}")

# 13- Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. 
# Haciendo que el programa avise cuando se escriben valores negativos o nulos.
num_1 = int(input("Ingrese un número: "))
num_2 = int(input("Ingrese otro número: "))
mayor = num_1
menor = num_2
if num_2 > num_1:
    mayor = num_2
    menor = num_1
if num_1 <= 0 or num_2 <= 0:
    print("No ingrese valores negativos o nulos")
else:
    if mayor%menor == 0:
        print(f"El número {mayor} es múltiplo de {menor}")
    else:
        print(f"El número {mayor} NO es múltiplo de {menor}")

# 14- Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
# Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos 
# los números sean solución. Se recuerda que la fórmula de las soluciones es:
# x = -b / a
print("Ecuación a resolver: a . x + b = 0")
valor_a = int(input("Ingrese el valor de a: "))
valor_b = int(input("Ingrese el valor de b: "))
if valor_a != 0:
    valor_x = -valor_b / valor_a
    print("el valor de X es: ", valor_x)
else:
    print("No puede dividir por 0")

# 15- Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. 
# Si se  contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que 
# pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un 
# círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
opc = input("¿Desea calcular el area de un triángulo o de un círculo? [T/C]: ")
opc = opc.lower()
if opc == "t":
    b = float(input("Ingrese la base del triángulo: "))
    h = float(input("Ingrese la altura del triángulo: "))
    area = (b*h)/2
    print(f"El area del triángulo es {area:.2f}")
elif opc == "c":
    r = float(input("Ingrese el radio del círculo: "))
    import math
    area = math.pi * r**2
    print(f"El área del circulo es {area:.2f}")
else:
    print("La opción ingresada no es válida")

# 16- Haz una calculadora básica pida al usuario dos valores, a y b.
# Según la opción que desean, realizar la operación:
# Si operación es 1 entonces debemos ver el resultado de a + b
# Si operación es 2 entonces debemos ver el resultado de a * b
# Si operación es 3 entonces debemos ver el resultado de a - b
# Si operación es 4 entonces debemos ver el resultado de a / b
print("Ingrese 2 valores: ")
a = int(input())
b = int(input())
print("¿Que operación desea realizar?")
print("1- Suma")
print("2- Multiplicación")
print("3- Resta")
print("4- División")
op = input()
if op == "1":
    resul = a+b
    print("El resultado es: ", resul)
elif op == "2":
    resul = a*b
    print("El resultado es: ", resul)
elif op == "3":
    resul = a-b
    print("El resultado es: ", resul)
elif op == "4":
    resul = a/b
    print("El resultado es: ", resul)
else:
    print("La opción ingresada no es válida")

# 17- Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje 
# diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es 
# ninguno de esos, imprimir otro mensaje.
dia = input("¿Qué día de la semana es hoy? ")
dia = dia.lower()
if dia == "lunes":
    print(f"Hoy es {dia} ¡feliz inicio de semana!")

if dia == "viernes":
    print(f"Hoy es {dia} ¡feliz fin de semana!")

if dia == "martes" or dia == "miercoles" or dia == "miércoles" or dia == "jueves":
    print(f"Hoy es {dia}, a seguir trabajando.")

if dia == "sábado" or dia == "sabado" or dia == "domingo":
    print(f"Hoy es {dia}, a descansar.")

# 18- Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
# La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
# Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.
hrs_tt = float(input("Ingrese cuantas horas trabajó este mes: "))
sal_h = float(input("Ingrese el salario por hora: "))
sal_ex = sal_h + (sal_h * 0.1)
hrs_ex = abs(hrs_tt - 48)
hrs_t = hrs_tt - hrs_ex
sal_t = (sal_h * hrs_t) + (sal_ex * hrs_ex)
print(f"De un total de {hrs_tt} horas trabajadas, con {hrs_ex} horas extra. Su salario de este mes será de: ${sal_t}")

# 19- Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, 
# existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.
cantidad = int(input("Ingrese la cantidad de lápices que va a comprar: "))
total = cantidad * 60
if cantidad >= 1000:
    total = total - (total * 0.07)
    print("El precio total a pagar con un descuento del 7 por ciento es de: $", total)
else:
    print("El total a pagar es de: ", total)

# 20- Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o 
# igual a 6; caso contrario saldrá desaprobado.
nota_1 = float(input("Ingrese la nota 1: "))
nota_2 = float(input("Ingrese la nota 2: "))
nota_3 = float(input("Ingrese la nota 3: "))
nota_4 = float(input("Ingrese la nota 4: "))
promedio = (nota_1+nota_2+nota_3+nota_4)/4
if promedio >= 6:
    print(f"Tu nota es {promedio:.2f} ¡aprobaste!")
else:
    print(f"Tu nota es {promedio:.2f}, desaprobaste")
