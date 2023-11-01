# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import random

print("~ Adivinador de números (～￣▽￣)～ ~")
print(" Necesitamos un rango primero así que ---> ")

inici, fin  = None, None

#Manejo de errores
while True:
    try:        
        inicio = int(input("Deme su primer número porfis "))
        break
    except:
        print("Debe ser un número entero ╰（‵□′）╯ ")

while True:
    try:        
        fin = int(input("Deme su segundo número porfis "))
        break
    except:
        print("Debe ser un número entero ╰（‵□′）╯ ")


fin, inicio = max([inicio, fin]), min([inicio, fin])

numero_random = random.randint(inicio, fin)

while True:
    try:
        res = int(input("Ok ahora adivina el número owo "))
        if res == numero_random:
            print(f"Acertaste!! El número era {res}")
            continuar = input("Deseas continuar si/no ").lower()
            if continuar != 'si':
                print("Bueno, adiós o(*￣▽￣*)ブ ")
                break
            else:
                quit()
        else:
            print("Fallaste viejo diablo ＼（〇_ｏ）／ ")
            continuar = input("Deseas continuar si/no ").lower()
            if continuar != 'si':
                break
    except:
        print("Debe ser un número entero unu ")



    