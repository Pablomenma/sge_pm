#Crea un programa que pida al usuario dos números y una operación (suma, resta, multiplicación o división) y muestre el resultado.
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

operacion = input("que quieres hacer (suma, resta, multiplicacion, division): ").lower()

if operacion == "suma":
    resultado = num1 + num2
elif operacion == "resta":
    resultado = num1 - num2
elif operacion == "multiplicacion":
    resultado = num1 * num2
elif operacion == "division":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: no se puede dividir entre 0"
else:
    resultado = "Operación no válida"

print(f"Resultado: {resultado}")
