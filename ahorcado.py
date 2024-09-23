import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    #Seleccionar una palabra al azar de la lista de palabras válidas
    palabra = random.choice(palabras)

    while '.' in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()



def ahorcado():

    print("====================================================")
    print("¡Bievenidos(a) al juego de ahorcado!")
    print("====================================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedeario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra] 
        #Mostrar estado del ahoracado
        print(vidas_diccionario_visual[vidas])
        #Mostrar la letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        #Si la letra escogida por el usuario está en el abecedario y no está en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedeario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #Si letra está en la palabra
            #quitar la letra del conjunto de letras pendientes por adivinar. si no está en la palabra, quitar una vida.
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"\n Tu letra, {letra_usuario} no está en la palabra.")
        #Si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida")
    #El juego llega a esta línea cuando se adivina todas las letras de la palabra o cuando se agotan las vidas del jugador
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho la palabra era: {palabra}")
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra! {palabra}")

ahorcado()