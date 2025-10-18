
#Crea un programa que convierta entre grados Celsius, Fahrenheit y Kelvin. El usuario introducirá primero la cantidad y la unidad de origen, y después la unidad de destino.
num = float(input("Introduce una cantidad de temperatura: "))
origen = input("Introduce la unidad de origen (C, F, K): ").upper()
destino = input("Introduce la unidad de destino (C, F, K): ").upper()

if origen == "C":
    celsius = num
elif origen == "F":
    celsius = (num - 32) * 5/9
elif origen == "K":
    celsius = num - 273.15
else:
    print("Unidad de origen no válida")
    exit()

if destino == "C":
    resultado = celsius
elif destino == "F":
    resultado = celsius * 9/5 + 32
elif destino == "K":
    resultado = celsius + 273.15
else:
    print("Unidad de destino no válida")
    exit()

print(f"{num} {origen} equivalen a {resultado:.2f} {destino}")



###Crea un programa que pida al usuario un número entero y calcule la suma de todos sus dígitos.

```python
entero = input("Introduce un número : ")

resultado = 0

for digito in entero:
    resultado += int(digito)

print(f"La suma de los dígitos de {entero} es {resultado}")
```


###Crea un programa que pida al usuario dos números y una operación (suma, resta, multiplicación o división) y muestre el resultado.

```Python
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
```

###Crea un programa que convierta entre grados Celsius, Fahrenheit y Kelvin. El usuario introducirá primero la cantidad y la unidad de 
origen, y después la unidad de destino.

```python
num = float(input("Introduce una cantidad de temperatura: "))
origen = input("Introduce la unidad de origen (C, F, K): ").upper()
destino = input("Introduce la unidad de destino (C, F, K): ").upper()

if origen == "C":
    celsius = num
elif origen == "F":
    celsius = (num - 32) * 5/9
elif origen == "K":
    celsius = num - 273.15
else:
    print("Unidad de origen no válida")
    exit()

if destino == "C":
    resultado = celsius
elif destino == "F":
    resultado = celsius * 9/5 + 32
elif destino == "K":
    resultado = celsius + 273.15
else:
    print("Unidad de destino no válida")
    exit()

print(f"{num} {origen} equivalen a {resultado:.2f} {destino}")

```


###Crea un programa que genere una contraseña aleatoria de una longitud que indique el usuario. La contraseña debe incluir letras mayúsculas, minúsculas, números y símbolos especiales.

```Python

import string

longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = "".join(random.choice(caracteres) for _ in range(longitud))

# Paso 4: mostrarla
print(f"Tu contraseña generada es: {contraseña}")

```

