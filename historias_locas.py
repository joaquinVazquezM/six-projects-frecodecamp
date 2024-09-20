#Concatenar cadenas de caracteres
#Supongamos que queremos crear una cadena que diga:
#Aprende a programar con __________________.

# organizacion = "freeCodeCamp"

# print("Aprende a programar con " + organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprender a programar con {organizacion}")

#Mad Libs (Historias locas)
print("--------------------------------------------------------------------------------------------")
print("Juego 'Palabras Locas'")
print("Se te presenta un texto donde te solicitar lo siguiente")
print("--------------------------------------------------------------------------------------------")
print("¡Programar es tan 'Ingresa una palabra (Adjetivo)'! Siempre me emociona por que me encanta 'Ingresa tu verbo' problemas. Aprender a 'Ingresa otro verbo' con freeCodeCamp y alcanza tus 'Ingresa un sustantivo en plural'")
adjetivo= input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo plural: ")

madlib = f"¡Programar es tan {adjetivo}! Siempre me emociona por que me encanta {verbo1} problemas. Aprender a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}"

print(madlib)