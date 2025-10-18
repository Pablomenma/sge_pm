#Crea una función que decodifique una cadena que ha sido comprimida usando el método RLE.
def decodificar_rle(texto):
    descifrado = ""
    numero = ""

    for letra in texto:
        if letra.isdigit():
            numero += letra
        else:
            descifrado += letra * int(numero)
            numero = ""  # Reiniciamos el número

    return descifrado


# Ejemplo de uso
texto_codificado = input("Escribe una cadena codificada en RLE (ejemplo: 3a2b1c4d): ")
texto_decodificado = decodificar_rle(texto_codificado)
print("Cadena decodificada:", texto_decodificado)
