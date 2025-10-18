#Escribe un programa que reciba una cadena y devuelva la longitud de la palabra más larga

texto = input("Escribe una frase: ")

palabras = texto.split()

if len(palabras) > 0:
    palabra_mas_larga = max(palabras, key=len)
    longitud = len(palabra_mas_larga)

    print("La palabra más larga es:", palabra_mas_larga)
    print("Su longitud es:", longitud)
else:
    print("No se ingresaron palabras.")
