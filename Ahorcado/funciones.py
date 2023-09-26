def assemble_word(word2,letter2,aux_word2):
    counter = 0
    word_string = ""
    for i in word2:
        if letter2 == i:
            aux_word2[counter] = letter2
        counter += 1
    print("La letra '"+letter2+"' se encuentra en la palabra!")
    print("")
    for i in aux_word2:
            word_string += i 
    return word_string

def letter_in_word(word1, letter1):
    for i in word1:
        if letter1 == i:
            return True

