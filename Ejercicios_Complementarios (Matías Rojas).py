# Ejercicios complementarios - Matías Rojas - Comisión B/3

#Variables principales

numero1 = 8
numero2 = 12.3
nombre = "Matías"
apellido = "Rojas"
precio = 4650
descuento = 0.2
cadena = "Hola mundo"
longitud = len(cadena)
precio2 = 34.67
edad = 18
altura = 1.76
nombremayus = "MATÍAS"

#Variables secundarias

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
precio_final = precio * descuento
nombre_completo = nombre + apellido
edad += 5
edad -= 10
altura *= 4
altura /= 3

#Impresiones

print("suma: ", suma) 
print("resta: ", round(resta,2))
print("multiplicación: ", multiplicacion)
print("división: ", round(division,2))
print("precio final: ", precio_final)
print("cadena: ", cadena)
print("longitud cadena: ", longitud)
print("precio: ", int(precio2))
print("nombre completo: ", nombre_completo)
print("edad: ", edad)
print("altura: ", round(altura, 2))
print("nombre minúsculas: ", nombremayus.lower())
print("nombre: ", nombremayus.capitalize())