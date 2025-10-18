#Crea una función que cuente cuántas palabras hay en una cadena, suponiendo que las palabras están separadas por espacios.
def contar_palabras(cadena):
    palabras = cadena.split()
    # Contamos cuántas hay
    return len(palabras)



# Ejemplo de uso
texto = input("Escribe una frase: ")
print("Número de palabras:", contar_palabras(texto))
