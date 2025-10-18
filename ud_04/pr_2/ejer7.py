#Escribe una función que rote una cadena hacia la izquierda un número dado de veces.
#Ejemplo: "abcdef" rotado 2 veces convierte la cadena en "cdefab".
def rotatexto(texto, n):
    n = n % len(texto)
    return texto[n:] + texto[:n]

texto = input("Escribe un texto: ")
veces = int(input("¿Cuántas veces quieres rotarla a la izquierda?: "))

resultado = rotatexto(texto, veces)
print("La cadena rotada es:", resultado)