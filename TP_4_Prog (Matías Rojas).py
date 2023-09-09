# 1. 
x = 0
while x < 30:
    x += 1
    if x == 15:
        print("The execution of the loop was broken when x was: ",x)
        break
    if x == 4 or x == 6 or x == 10:
        print("The value ",x," of x was skipped")
        continue
    print("The value of the loop is: ", x)
    

# 1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. 
# Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.
line = ""
while line != " ":
    
    line = input("Ingrese una línea de texto: ")
    if line == " " or line == "":
        break
    line = line.upper()
    print("La línea ingresada es: "+line)
    print("Para terminar deje la línea en blanco")

# 2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
# La bitácora de operaciones tiene la siguiente forma:
# D 100
# R 50

# D 100 significa que depositó 100 pesos
# R 50 significa que retiró 50 pesos

# Ejemplo de una entrada:
# D 200
# D 200
# R 100
# D 50
# Introducir una línea vacía indica que ha finalizado la bitácora.
# La salida de éste programa sería:
# 350
account = 0
action = ""
print("Ingrese 'D [num]' para depositar dinero")
print("Ingrese R [num] para retirar dinero")
print("Para finalizar introduzca una línea vacía:")
while action != " ":
    action = input()
    if action== "" or action== " ":
        break
    action = action.upper()
    action = action.split()
    
    if action[0] == "D":
        print(f"Depositó {action[1]} pesos")
        account += int(action[1])
    elif action[0] == "R":
        print(f"retiró {action[1]} pesos")
        account -= int(action[1])
    else:
        print(f"{action[0]} no es una acción válida")
print(f"Su cuenta tiene {account} pesos almacenados")

# 3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad total de números primos ingresados.
num = 1
prime_nums = 0
print("Ingrese números mayores a 1")
print("Para terminar, ingrese un 0: ")
while num != 0:
    num = int(input())
    if num == 0:
        break
    if num == 1: 
        continue
    if num % num == 0 and num % 1 == 0 and num % 2 != 0 and num % 3 != 0:
        prime_nums += 1
    if num == 2 or num == 3:
        prime_nums += 1
print(prime_nums)

# 4.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, 
# que sean bisiestos y múltiplos de 10. Nota: Para que un año sea bisiesto debe ser divisible por 4 y no 
# debe ser divisible por 100, excepto que también sea divisible por 400.
years = input("Ingrese 2 años: [año1 año2]: ")
years = years.split()
year1 = int(years[0])
year2 = int(years[1])
if year1 > year2:
    year1 = int(years[1])
    year2 = int(years[0])
print(f"Años bisiestos y múltiplos de 10 entre {year1} y {year2}")
while year1 < year2:
    if year1 % 4 == 0 and year1 % 100 != 0:
        print(year1)
        year1 += 1
        continue
    if year1 % 4 == 0 and year1 % 400 == 0:
        print(year1)
        year1 += 1
        continue
    if year1 % 10 == 0:
        print(year1)
        year1 += 1
        continue
    year1 += 1

# 5.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. 
# Utiliza la declaración continue para omitir los números impares.
for num in range(1,20+1):
    if num % 2 != 0:
        continue
    print(num)

# 6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. 
# Cuando encuentres el número, usa break para salir del bucle.
numlist = []
listlong = int(input("Ingrese el largo deseado de la lista de números: "))
for i in range(1,listlong+1):
    numlist.append(i)
findnum = int(input("Ingrese el número que desea encontrar en la lista: "))
for i in numlist:
    if i == findnum:
        break
print("Número encontrado!")

# 7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). 
# Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", 
# utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).
from datetime import date
option = 1
print("Bienvenido al menú de opciones!")
print("Seleccione una opción: ")
while option != 0:
    print("0. Cerrar menú")
    print("1. Mostrar hola mundo")
    print("2. Mostrar suma de 1+1")
    print("3. Mostrar la fecha de hoy [año/mes/día]")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        print("Hola mundo!")
    if option == 2:
        print("la suma de 1+1 es: ", 1+1)
    if option == 3:
        print("La fecha de hoy es: ", date.today())
print("Hasta luego!")