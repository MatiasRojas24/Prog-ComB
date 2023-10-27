# 3.	Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para 
# inicializar los atributos, imprimir el valor del lado con un tamaño mayor y
# el tipo de triángulo que es (equilátero, isósceles o escaleno).
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def triangle_type(self):
        if self.__side_a == self.__side_b == self.__side_c:
            return "equilátero"
        elif self.__side_a == self.__side_b or self.__side_a == self.__side_c or self.__side_b == self.__side_c:
            return "isósceles"
        else:
            return "escaleno"
    
    def larger_side(self):
        larger_triangle_side = self.__side_a
        if larger_triangle_side < self.__side_b:
            larger_triangle_side = self.__side_b
        if larger_triangle_side < self.__side_c:
            larger_triangle_side = self.__side_c
        return larger_triangle_side
