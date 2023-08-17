# 1. Calcular el perímetro y área de un rectángulo dada su base y su altura.
print("1.")
base = 4
altura= 2
perimetro = 2 * (base + altura)
area = base * altura
print("El perimetro del rectángulo es: ", perimetro)
print("El area del rectángulo es: ", area)

# 2. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
print("2.")
cateto1 = int(input("Ingrese el cateto 1: "))
cateto2 = int(input("Ingrese el cateto 2: "))
hipotenusa = (cateto1 ** 2) + (cateto2 ** 2)
hipotenusa = hipotenusa ** 0.5
print(f"el valor de la hipotenusa es: {hipotenusa:.2f}")

# 3. Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
print("3.")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {mult}")
print(f"{num1} / {num2} = {div:.2f}")

# 4. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
print("4.")
grados_f = float(input("Ingrese grados fahrenheit: "))
grados_c = (grados_f - 32) * (5/9)
print(f"El valor en grados celsius es: {grados_c:.2f}°")

# 5. ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?
print("5.")
# a) A = input(nombre, "¿Cuál es tu canción favorita?")
print("a)")
cancion_favorita = input("¿Cuál es tu canción favorita? ")
# b) precio = input(“Precio: “)
#    total = precio + (precio * 0.1)
precio = float(input("Precio: "))
total = precio - (precio * 0.1)
# c) edad = int(input(“Edad: “))
#    print(tu edad es, edad)
print("c)")
edad = int(input("Edad: "))
print("tu edad es: ", edad)
# d) edad = int(input(“Edad: “))
#    print(“Veamos si tu edad es 18…”, edad=18)
print("d)")
edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad==18)

# 6. Calcular la media de tres números pedidos por teclado.
print("6.")
num1= float(input("Ingresa el primer número: "))
num2= float(input("Ingresa el segundo número: "))
num3= float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números ingresados es: {promedio:.2f}")

# 7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. 
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
print("7.")
minutos = int(input("Ingrese la cantidad de minutos: "))
horas = int(minutos/60)
mins = minutos%60
print(f"{horas} horas y {mins} minutos")

# 8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por 
# concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes 
# tomando en cuenta su sueldo base y comisiones.
print("8.")
sueldo_base = 70000
extra = .10
total = sueldo_base + sueldo_base * (extra * 3)
print ("El total que recibirá el empleado en el mes es de: $", total)

# 9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
print("9.")
compra = float(input("Ingrese el precio de su compra: "))
descuento = 0.15
precio_final = compra - (compra * descuento)
print("El precio final de su compra es: ", precio_final)

# 10.Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes 
# porcentajes:
#    55% del promedio de sus tres calificaciones parciales.
#    30% de la calificación del examen final.
#    15% de la calificación de un trabajo final.
print("10.")
parcial_1 = float(input("Ingrese la calificación del primer parcial: "))
parcial_2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial_3 = float(input("Ingrese la calificación del tercer parcial: "))
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))
punt_max_total = (30 * 0.55) + (10 * 0.3) + (10 * 0.15)
promedio = (parcial_1 + parcial_2 + parcial_3) / 3
calific_final = promedio - (promedio * 0.55) 
calific_final += examen_final - (examen_final * 0.3)
calific_final += trabajo_final - (trabajo_final * 0.15)
calific_final /= punt_max_total
print(f"Tu calificación final es de: %{(calific_final * 100):.0f} o {(calific_final * 10):.2f}")

# 11. Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea 
# siempre positivo).
print("11.")
num_1 = float(input("Ingrese un número: "))
num_2 = float(input("Ingrese otro número: "))
dist = abs((num_1 - num_2))
print(f"La distancia entre los dos números es de: {dist:.2f}")

# 12. Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
print("12.")
num = float(input("Ingrese un número: "))
raiz_cuadrada = num ** 0.5
raiz_cubica = num ** (1/3)
print(f"La raíz cuadradra del número {num} es: {raiz_cuadrada:.2f} y su raíz cúbica es: {raiz_cubica:.2f}")

# 13. Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si introduce 23 que muestre 32.
print("13.")
numero = input("Ingrese un número: ")
long = len(numero)
invertido = ""
while long != 0:
    invertido += str(numero[long-1])
    long -=1
print("El invertido del número ingresado es: ", invertido)

# 14. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de 
# ambas variables y muestre cuánto valen al final las dos variables.
print("14.")
A = input("Ingrese el valor de la variable A: ")
B = input("Ingrese el valor de la variable B: ")
C = A
A = B
B = C
print("El valor de la variable A es: ", A)
print("El valor de la variable B es: ", B)