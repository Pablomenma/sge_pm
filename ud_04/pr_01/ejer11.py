#calcular el factorial de un numero.
num = int(input("Introduce un número entero: "))

resultado = 1
for i in range(1, num + 1):
    resultado *= i   
print(f"El factorial de {num} es {resultado}")
