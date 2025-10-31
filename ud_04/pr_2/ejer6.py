#Escribe un programa que convierta las letras minúsculas de una cadena en mayúsculas y viceversa.
texto = input("introduce un texto")
salida = ""
    
    for caracter in texto:
        if caracter.islower():      # si es minúscula
            salida += caracter.upper()
        elif caracter.isupper():    # si es mayúscula
            salida += caracter.lower()
        else:                       # si no es letra (espacio, número, etc.)
            salida += caracter
            print(salida)