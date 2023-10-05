from TP5progFunc import valid_dni, long_word, id_club, is_multiple_of, average_temperature, extra_space, min_max_num, area_perimeter_circumference, login, buy_discount, list_reciever, dictionary_words_and_length, vector_module, is_prime_num, factorial, digit_in_number, digit_sum
import pytest
# ejemplo prueba
# def test_valid_dni():
#    assert valid_dni("46396605")
# @pytest.mark.parametrize("input_x, expected",[("46396605", True), ("4782093", True), ("202", False)])

# Pruebas 1-
@pytest.mark.parametrize("input_x, expected",[
    ("46396605", True),
    ("4782093", True),
    ("202", False)
])
def test_valid_dni_params(input_x, expected):
    assert valid_dni(input_x) == expected

# Pruebas 2- 
@pytest.mark.parametrize("input_word, expected",[
    ("Hola mundo", 5),
    ("Testeando en python", 6),
    ("Milanesa a la napolitana", 10),
])
def test_long_word(input_word, expected):
    assert long_word(input_word) == expected

# Pruebas 3-
@pytest.mark.parametrize("input_full_name, input_dni, expected",[
    ("Matías Emanuel Rojas","46396605","Matías5463"),
    ("Renzo López","35467906","Renzo5354"),
    ("Regina Torres","49325430","Regina6493")
])
def test_id_club(input_full_name, input_dni, expected):
    assert id_club(input_full_name, input_dni) == expected

# Pruebas 4- 
@pytest.mark.parametrize("input_num, input_multiple, expected",[
    (2,4,True),
    (6,36,True),
    (2,9,False)
])
def test_is_multiple_of(input_num, input_multiple, expected):
    assert is_multiple_of(input_num, input_multiple) == expected

# Pruebas 5-
@pytest.mark.parametrize("input_min_temp, input_max_temp, expected",[
    (20,32,((20+32)/2)),
    (2,15,((2+15)/2)),
    (7,23,((7+23)/2))
])
def test_average_temperature(input_min_temp, input_max_temp, expected):
    assert average_temperature(input_min_temp, input_max_temp) == expected

# Prueba 6-
@pytest.mark.parametrize("input_string, expected",[
    ("Hola mundo!","H o l a   m u n d o ! "),
    ("Python","P y t h o n ")
])
def test_extra_space(input_string, expected):
    assert extra_space(input_string) == expected

# Prueba 7-
@pytest.mark.parametrize("input_numlist, expected",[
    ([2,7,3,9],(9,2)),
    ([1,8,14],(14,1)),
    ([8,9,15,27,-1],(27,-1))
])
def test_min_max_num(input_numlist, expected):
    assert min_max_num(input_numlist) == expected

# Prueba 8-
@pytest.mark.parametrize("input_rad, expected",[
    (2.6,area_perimeter_circumference(2.6)),
    (8,area_perimeter_circumference(8)),
    (12.53,area_perimeter_circumference(12.53))
])
def test_area_perimeter_circunference(input_rad, expected):
    assert area_perimeter_circumference(input_rad) == expected

# Prueba 9-
@pytest.mark.parametrize("input_user, input_pass, tries, valid",[
    ("usuario1","asdasd",3,(True,3)),
    ("usuario1","asdasd",1,(True,1)),
    ("Matías","12343",2,(False,1))
])
def test_login(input_user, input_pass, tries,valid):    
    assert login(input_user, input_pass, tries) == valid

# Prueba 10-
@pytest.mark.parametrize("input_buyed_items, expected",[
    ({'Licuadora':{'precio':34389.52, 'descuento':10}, 'Tostadora':{'precio':13998, 'descuento':5}}, 44248.668),
    ({'Memoria RAM':{'precio':15500, 'descuento':10}, 'Procesador':{'precio':75480, 'descuento':20}, 'Placa Madre':{'precio':95000, 'descuento':15}, 'Monitor':{'precio':35200, 'descuento':5}, 'Teclado':{'precio':13000, 'descuento':5}, 'Mouse':{'precio':9998, 'descuento':5}}, 210372.1)
])
def test_buy_discount(input_buyed_items, expected):
    assert buy_discount(input_buyed_items) == expected
# Prueba 11-
@pytest.mark.parametrize("input_list, expected",[
    ([1.5, 2, 6, 8, 23], [15, 20, 60, 80, 230]),
    (["Hola mundo", "Python", "Test"],["Hola mundo!", "Python!", "Test!"]),
    ([False, True, False], [True, False, True]),
    ([7.6, 42, "Lista", True], [76, 420, "Lista!", False])
])
def test_list_reciever(input_list, expected):
    assert list_reciever(input_list) == expected

# Prueba 12- 
@pytest.mark.parametrize("input_phrase, expected",[
    ("Hola mundo", {'hola':4, 'mundo':5}),
    ("Programando en python", {'programando':11, 'en':2, 'python':6}),
    ("Milanesas caseras a la napolitana con papas al horno", {'milanesas':9,'caseras':7,'a':1,'la':2,'napolitana':10,'con':3,'papas':5,'al':2,'horno':5})
])
def test_dictionary(input_phrase, expected):
    assert dictionary_words_and_length(input_phrase) == expected

# Prueba 13-
@pytest.mark.parametrize("input_coord_a, input_coord_b, expected",[
    (3,7,vector_module(3,7)),
    (10,2,vector_module(10,2)),
    (1,23,vector_module(1,23))
])
def test_vector_module(input_coord_a, input_coord_b, expected):
    assert vector_module(input_coord_a, input_coord_b) == expected

# Prueba 14-
@pytest.mark.parametrize("input_num, expected",[
    (31, True),
    (75, False),
    (83, True),
    (97, True),
    (33, False),
    (1, False),
    (61, True),
    (89, True),
    (100, False),
    (99, False)
])
def test_is_prime_num(input_num, expected):
    assert is_prime_num(input_num) == expected
# Prueba 15-
@pytest.mark.parametrize("input_num, expected",[
    (2, 2),
    (0, 1),
    (7, 5040),
    (10, 3628800),
    (-1, None)
    ])
def test_factorial(input_num, expected):
    assert factorial(input_num) == expected

# Prueba 16-
@pytest.mark.parametrize("input_num, input_digit, expected",[
    ("2022", "2", 3),
    ("502335129", "3", 2),
    ("11011101", "1", 6),
    ("3439821", "6", 0),
    ("9990", "0", 1),
    ])
def test_digit_in_number(input_num, input_digit, expected):
    assert digit_in_number(input_num, input_digit) == expected

# Prueba 17-
@pytest.mark.parametrize("input_num, expected",[
    ("1101", 3),
    ("205231", 13),
    ("91834", 25),
    ("0000", 0),
    ("2453215260", 30)
    ])
def test_digit_sum(input_num, expected):
    assert digit_sum(input_num) == expected
# reutilizo las funciones:
# digit_in_number
# factorial
# is_prime_num