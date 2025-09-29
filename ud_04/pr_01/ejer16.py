#Crea un programa que pida al usuario un número entero y calcule la suma de todos sus dígitos.
entero = input("Introduce un número : ")

resultado = 0

for digito in entero:
    resultado += int(digito)

print(f"La suma de los dígitos de {entero} es {resultado}")
