import random, funciones
words = ["palabra", "teclado", "programacion", "codigo", "procesador", "monitor", "fuente", "python"]
word = words[random.randint(0,len(words)-1)]
aux_hidden_word = []
hidden_word = ""
letter = ""
lives = 6
is_in_word = False

for i in word:
    aux_hidden_word.append("_")
while lives != 0 or hidden_word != word:
    counter = 0
    is_in_word = False
    print("Estado de la palabra: ",hidden_word)
    print("Vidas restantes: ", lives)
    letter = input("Ingrese una letra: ")
    is_in_word = funciones.letter_in_word(word, letter)
    if is_in_word:
        hidden_word = funciones.assemble_word(word,letter,aux_hidden_word) 
    else:
        lives -= 1
        print("La letra '"+letter+"' no se encuentra en la palabra :(")
        print("Perdiste una vida!")
        print("")
    
    if lives == 0:
        print("Perdiste todas tus vidas, suerte para la próxima")
        break
    if hidden_word == word:
        print("Adivinaste la palabra: '"+hidden_word+"' felicidades!")
        break