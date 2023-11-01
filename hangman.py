# The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability, so line 1 in program imports it.
# The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
# When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over. 
# For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.

import random

palabras = ["manzana", "perro", "guitarra", "sol", "bicicleta", "python", "playa", "libro", "montaña", "familia"]

palabra_aleatoria = random.choice(palabras)
aciertos = []
intentos = 15

def mostrar_letras(aciertos: list):
    nueva_palabra = ""

    #Forma orizontal
    for letra in palabra_aleatoria:
        if letra in aciertos:
            nueva_palabra += letra
        else:
            nueva_palabra += "_ "
    
    if nueva_palabra == palabra_aleatoria:
        print(nueva_palabra)
        print("¡Felicidades! Has ganado la partida")
        quit()
    print(nueva_palabra)


    ##Forma vertical
    # for i in palabra_aleatoria:
    #     if i in aciertos:
    #         print(i)
    #     else: 
    #         print("_")
    
while intentos > 0:
    mostrar_letras(aciertos)

    while True:
        try:        
            letra = str(input("deme su letra owo "))
            break
        except:
            print("Debe ser una letra ╰（‵□′）╯ ")
    
    if letra in palabra_aleatoria:
        aciertos.append(letra)
    else:
        print("="*20)
        print("Que aweonao se equivocó ")
        print("="*20)

    intentos -= 1

    