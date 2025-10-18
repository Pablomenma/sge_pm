#Escribe una función que reciba una cadena y cuente cuántas vocales y consonantes contiene.
def contar_vocales_consonantes(texto):
    texto = texto.lower()
    
    vocales = "aeiou"
    contvocal = 0
    contconsonante = 0
    
    for caracter in texto:
        if caracter.isalpha():  # Solo contamos letras (ignoramos espacios, números, signos)
            if caracter in vocales:
                contvocal += 1
            else:
                contconsonante += 1
    
    return contvocal, contconsonante

# Ejemplo de uso
texto = "Hola mundo"
v, c = contar_vocales_consonantes(texto)
print(f"Vocales: {v}, Consonantes: {c}")
