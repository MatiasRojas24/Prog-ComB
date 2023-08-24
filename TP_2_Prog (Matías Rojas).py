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

# 17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje 
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
