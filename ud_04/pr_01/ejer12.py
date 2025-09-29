#Crea un programa que solicite al usuario una cadena de texto y muestre cuántas vocales y cuántas consonantes contiene.
entrada = input("Introduce un texto: ")

vocales = "aeiou"

contvocales = 0
contconsonantes = 0

for letra in entrada:
    if letra.isalpha():  # verificamos que sea letra
        if letra in vocales:
            contvocales += 1
        else:
            contconsonantes += 1

# Paso 4: mostrar resultados
print(f"Número de vocales: {contvocales}")
print(f"Número de consonantes: {contconsonantes}")
