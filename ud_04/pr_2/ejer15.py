#Escribe una función que compare dos cadenas sumando el valor ASCII de cada carácter y devuelva cuál tiene un mayor valor total. Para este ejercicio ten en cuenta que la función integrada ord() devuelve el valor ASCII de un carácter
def comparar_cadenas_ascii(cadena1, cadena2):
    suma1 = sum(ord(c) for c in cadena1)
    suma2 = sum(ord(c) for c in cadena2)

    # Mostrar los resultados
    print(f"Valor total de '{cadena1}': {suma1}")
    print(f"Valor total de '{cadena2}': {suma2}")

    # Comparar y devolver resultado
    if suma1 > suma2:
        return f"La cadena con mayor valor ASCII es: '{cadena1}'"
    elif suma2 > suma1:
        return f"La cadena con mayor valor ASCII es: '{cadena2}'"
    else:
        return "Ambas cadenas tienen el mismo valor total ASCII."


# Ejemplo de uso
texto1 = input("Escribe la primera cadena: ")
texto2 = input("Escribe la segunda cadena: ")

resultado = comparar_cadenas_ascii(texto1, texto2)
print(resultado)
