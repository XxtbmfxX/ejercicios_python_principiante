# Two players play the game against each other; let’s assume Player 1 and Player 2.

# Player 1 plays first by setting a multi-digit number.
# Player 2 now tries his first attempt at guessing the number.
# If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
# The game continues till Player 2 eventually is able to guess the number entirely.
# Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
# If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
# If not, then Player 2 wins the game.
# The real game, however, has proved aesthetics since the numbers are represented by color-coded buttons.

# Input:

# Player 1, set the number: 5672
# Player 2, guess the number: 1472
# Output:

# Not quite the number. You did get 2 digits correct.
# X X 7 2

# Enter your next choice of numbers:

import random


def preguntar_continuar():
    while True:
        try:
            continuar = input("Desea seguir jugando? si/no ")
            if continuar.lower() not in ['si', 'no']:
                raise ValueError
            return continuar
        except ValueError:
            print("SI O NO >:( )")

def obtener_numero():
    while True:
        try:
            numero = int(input("Ingresa un número: "))
            return numero
        except ValueError:
            print("Por favor, ingresa un número válido.")

def comparar_digitos(num1, num2):
    # Convierte los números en cadenas
    str_num1 = str(num1)
    str_num2 = str(num2)
    res = ""

    # Compara los dígitos
    for digito1, digito2 in zip(str_num1, str_num2):
        if digito1 == digito2:
            res += digito1
        else:
            res += "X"

    return res

def main():
        
    print("\n ~ MAASTERMIND ~ \n")
    print("owo Adivina el número owo")

    while True:

        pc = random.randint(1, 2000)
        print(pc)

        numero_ingresado = obtener_numero()

        comparacion = comparar_digitos(numero_ingresado, pc)

        if "X" in comparacion:
            print("Cielos viejo eso estuvo cerca")
            print(f"\n {comparacion} \n")
        else:
            print("Diablos eres un adivino")
            print(f"\n {comparacion} \n")


        continuar = preguntar_continuar()

        if continuar != "si":
            break
        

if __name__ == "__main__":
    main()