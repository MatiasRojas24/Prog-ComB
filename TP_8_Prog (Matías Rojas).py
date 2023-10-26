# 1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
def digits(n):
    if n < 10:
        return 1
    else:
        return 1 + digits(n/10)
num = int(input("Ingrese un número: "))
print(f"El número ingresado tiene {digits(num)} dígitos")

# 2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.
def n_power_of_b(n,b):
    if n > b:
        return n_power_of_b(n/b,b)
    if n == b:
        return True
    if n < b:
        return False

b_input = int(input("Ingrese un número: "))
print("Ingrese un número que sea potencia de", b_input)
n_input = int(input())
if n_power_of_b(n_input, b_input):
    print(f"{n_input} es potencia de {b_input}")
else:
    print(f"{n_input} no es potencia de {b_input}")

# 3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista 
# con las posiciones en donde se encuentra b dentro de a. Ejemplo:
def positions(a, b, i=0):
    if len(a) < len(b):
        return []
    elif a[:len(b)] == b:
        return [i] + positions(a[len(b):], b, i+len(b))
    else:
        return positions(a[1:], b, i+1)

print(positions("Un tete a tete con Tete", "te"))

# 4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del 
# numero natural dado, conociendo solo que:
# •	1 es impar.
# •	Si un número es impar, su antecesor es par; y viceversa.
def pair(n):
    if n == 1:
        return False
    else:
        return odd(n - 1)

def odd(n):
    if n == 1:
        return True
    else:
        return pair(n - 1)

print(pair(6))
print(odd(6))

# 5.	Escribir una función recursiva que encuentre el mayor elemento de una lista.
def max_element(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return max(lista[0], max_element(lista[1:]))

print(max_element([3,6,2,9,5,7,1]))

# 6.	Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. 
# Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])
def replicate_element(elements_list, rep_x_times):
    if elements_list == [] or rep_x_times == 0:
        return []
    else:
        return [elements_list[0]]*rep_x_times + replicate_element(elements_list[1:],rep_x_times)
num_list = [1,3,3,7]
reps = 2
pos = 0
print(replicate_element(num_list,reps))

# 7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente sumatoria:
# K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
# ● El programa debe pedir al usuario que ingrese un número n, y un número d,
# ● Luego debe calcular el valor de K(n, p) usando una función recursiva,
# ● Debe imprimir el resultado de K(n, p)
def calculate_sumatory(n, p):
    if n == 1:
        return p
    else:
        return n * p + calculate_sumatory(n - 1, p)

n = int(input("Ingrese el valor de n: "))
p = int(input("Ingrese el valor de p: "))
result = calcular_sumatoria(n, p)
print(f"El valor de K({n}, {p}) es: {result}")

# 8.	El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: 
# Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 
# (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos unos. Cualquier 
# otro valor se calcula sumando los dos valores contiguos de la fila de arriba. Escribí la función recursiva 
# pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

row = 6
column = 4
value = pascal(row, column)
print(f"El valor en la fila {row} y la columna {column} en el Triángulo de Pascal es: {value}")

# 9.	Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un 
# número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados (permitiendo 
# caracteres repetidos).
def combinations(list, k, string=""):
    if k == 0:
        print(string)
        return
    for char in list:
        combinations(list, k - 1, string + char)

chars = ['a','b']
num = 2
combinations(chars, num)

# 10.	La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 
# (210 mm de ancho y 297 mm de largo). Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 
# las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N). Siempre se miden en 
# milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.
def medidas_hoja_A(N):
    if N == 0:
        return (1189,841 )
    else:
        previous_width, previous_lenght = medidas_hoja_A(N - 1)
        if N % 2 == 0:
            previous_width = previous_width
            previous_lenght = previous_lenght/2
        else:
            previous_width = previous_width/2 
            previous_lenght = previous_lenght
        return (int(previous_width), int(previous_lenght))

N = 4
width, lenght = medidas_hoja_A(N)
print(f"Las medidas de la hoja A({N}) son: Ancho = {width} mm, Largo = {lenght} mm")
