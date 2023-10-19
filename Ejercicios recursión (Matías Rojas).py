# 1. Escribir una función que simule el siguiente experimento: Se tiene una rata en una 
# jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma 
# probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5 
# minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula. 
# La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero 
# quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
# La función debe devolver el tiempo que tarda la rata en salir de la jaula.
import random
def rat_experiment(time_spent):
    path = random.randint(1,3)
    if path == 3:
        time_spent += 7
        return time_spent
    if path == 2:
        time_spent += 5
        return rat_experiment(time_spent)
    if path == 1:
        time_spent += 3
        return rat_experiment(time_spent)

print(f"La rata ha tardado {rat_experiment(0)} minutos en salir de la jaula")

# 2. Escribir una consigna apropiada para la siguiente función. Asumir que n es un número 
# entero
def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

num = int(input("Ingrese el número que desea invertir: "))
print(f"El número {num} invertido es: {f(num)}")
