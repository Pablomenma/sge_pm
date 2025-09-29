#Crea un programa que pida al usuario que introduzca 5 números y luego le diga cuál es el mayor y el menor de todos ellos de la forma: El número mayor es <mayor> y el menor es <menor>
# lista donde guardo los numeros introducidos por el usuario
numeros = []
# Pedir 5 números al usuario
for i in range(5):
    numero = int(input(f"Introduce el número {i+1}: "))
    numeros.append(numero)
# Calcular el mayor y el menor
mayor = max(numeros)
menor = min(numeros)

# Mostrar el resultado
print(f"El número mayor es {mayor} y el menor es {menor}")

