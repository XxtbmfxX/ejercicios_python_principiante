# https://www.geeksforgeeks.org/21-number-game-in-python/ 


# 21, Bagram, or Twenty plus one is a game which progresses by counting up 1 to 21, with the player who calls “21” is eliminated. It can be played between any number of players. Implementation This is a simple 21 number game using Python programming language. The game illustrated here is between the player and the computer. There can be many variations in the game.

# The player can choose to start first or second.
# The list of numbers is shown before the Player takes his turn so that it becomes convenient.
# If consecutive numbers are not given in input then the player is automatically disqualified.
# The player loses if he gets the chance to call 21 and wins otherwise.
# Winning against the computer can be possible by choosing to play second. The strategy is to call numbers till the multiple of 4 which would eventually lead to 21 on computer hence making the player the winner. 

#elegir priemero o segundo

import random

los_numeros = []

user_nums = []
pc_nums = []


#ingresar un número indefinido de números. menor a 3
def pc_random_inputs(los_numeros: list):
    if not los_numeros:  # Verifica si la los_numeros está vacía
        ultimo_numero = 1
    else:
        ultimo_numero = los_numeros[-1]
    
    longitud_secuencia = random.randint(1, 4)
    secuencia = [ultimo_numero + i for i in range(1, longitud_secuencia+1)]
    return secuencia


def user_random_inputs() -> list:
    print("\n=== Ingrese su lista de numeros ===")
    return [int(x) for x in input().split()]

def validar_entrada(lista, lista_previa):
    # Verificar que los números estén en el rango de 0 a 21
    if not all(0 <= num <= 21 for num in lista):
        return False, "Los números deben estar entre 0 y 21."

    # Verificar que la lista esté ordenada de menor a mayor
    if lista != sorted(lista):
        return False, "La lista no está ordenada de menor a mayor."

    # Comprobar que los números no estén en la lista previa
    if any(num in lista_previa for num in lista):
        return False, "Al menos uno de los números ya está en la lista previa."

    # Verificar si la lista previa no está vacía y comparar el último número
    if lista_previa and lista_previa[-1] >= lista[0] :
        return False, "El último número de la lista previa no es menor que el primer número ingresado."

    return True, "La lista es válida."

print("~ El juego del 21 ~")
print(" === Elige una cantidad de números a ingresar ===")
print(" === Si no están en orden pierdes owo ===")
print(" === Si llegas al 21 pierdes owo ===\n")



#validar oopción en un loop con try catch
usuario = input("Quiere ser empezar o ir segundo? (primero/segundo) ").lower()

while len(los_numeros) < 21:
    
    
    validacion = None

    #si la opción fue ir segundo llamamos a la función para elegir un número al azar de digitos a ingresar
    if usuario == "segundo":
        if not los_numeros:
            los_numeros.append(1)
        los_numeros += pc_random_inputs(los_numeros)
        print(los_numeros)


    usuario_inputs = user_random_inputs()
    validacion = validar_entrada(usuario_inputs, los_numeros)

    #validar datos de usuario
    if validacion[0] == True:
        print(validacion[1])

        los_numeros += usuario_inputs
        los_numeros += pc_random_inputs(los_numeros)
    
        
    if los_numeros[-1] >= 21:
        print("\nPerdió colega")
        print(los_numeros)
        print(f"\n{validacion[1]} \n\n")
        quit() 

    print(los_numeros)
        