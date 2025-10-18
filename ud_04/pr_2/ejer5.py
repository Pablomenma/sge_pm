#Escribe una función que elimine los caracteres duplicados en una cadena, manteniendo solo la primera aparición de cada uno.
def eliminar(texto):
    salida = ""   
    for letra in texto:
        if letra not in salida:   
            salida += letra
    return salida

# Ejemplo de uso
texto = input("Escribe un texto: ")
print("Texto sin duplicados:", eliminar(texto))
