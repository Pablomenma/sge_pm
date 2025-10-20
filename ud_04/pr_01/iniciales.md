# PRÁCTICAS SISTEMAS DE GESTIÓN EMPRESARIAL. PABLO MENDOZA MAYO

## Unidad 04: Python.


####Crea un programa que solicite un número por pantalla al usuario y siga pidiéndolo hasta que el usuario introduzca un número válido.


```python
entrada = input("Introduce un numero: ")

while(not entrada.isdigit()):
    entrada = input("Introduce un numero: ")

print("Has introducido un numero")
```

###Crea un programa que solicite un número n y un valor k y que muestre por la terminal los primeros k elementos de la tabla de multiplicar de n.

```python
n = int( input("Dime el valor n: ") )

k = int( input("Dime el valor k: ") )

for iter in range(1, k+1):

    print( f"{n} * {iter} = { n*iter }" )
```

####Crea un programa que solicite un número al usuario y dibuje un triángulo con asteriscos cuya base sea el número introducido.

```python
base = int(input("Introduce un número : "))

for i in range(1, base + 1):
    print("*" * i)
'''

### Modifica el programa anterior para que en lugar de crear un triángulo cree una pirámide. Si el usuario introduce un número par se lo volverá a pedir hasta que introduzca un número impar.

```python
base = int(input("Introduce un número impar: "))
while base % 2 == 0:   
    base = int(input("El número debe ser impar, inténtalo de nuevo: "))

lineas = base // 2 + 1   
for i in range(lineas):
    espacios = " " * (lineas - i - 1)         
    asteriscos = "*" * (2 * i + 1)           
    print(espacios + asteriscos)

```

###Crea un programa que convierta entre diferentes unidades de longitud (milímetros, centímetros, metros y kilómetros). El usuario introducirá primero la cantidad, luego la unidad de medida en que está y finalmente la unidad de medida a la que se va a convertir.

```python
cantidad = float(input("escribe una cantidad"))
```python
cantidad = int(input("introduce la unidad a la que quieres cambiar"))
unidad_inicial = input("Introduce la unidad de miedida inicial")
unidad_final = input("Introduce la unidad de medida final")

match unidad_final:
    case "mm":
        cantidad = (
            (cantidad * (10 ** 1)) if unidad_inicial == "cm" else
            (cantidad * (10 ** 3)) if unidad_inicial == "m" else
            (cantidad * (10 ** 6)) if unidad_inicial == "km" else
            cantidad
        )
    case "cm":
        cantidad = (
            (cantidad * (10 ** -1)) if unidad_inicial == "mm" else
            (cantidad * (10 ** 2)) if unidad_inicial == "m" else
            (cantidad * (10 ** 5)) if unidad_inicial == "km" else
            cantidad
        )
    case "m":
        cantidad = (
            (cantidad * (10 ** -2)) if unidad_inicial == "cm" else
            (cantidad * (10 ** -3)) if unidad_inicial == "mm" else
            (cantidad * (10 ** 3)) if unidad_inicial == "km" else
            cantidad
        )
    case "km":
        cantidad = (
            (cantidad * (10 ** -5)) if unidad_inicial == "cm" else
            (cantidad * (10 ** -3)) if unidad_inicial == "m" else
            (cantidad * (10 ** -6)) if unidad_inicial == "mm" else
            cantidad
        )

cantidad = round(cantidad)

print("Tu medida es: " + str(cantidad) + str(unidad_final))

```

####Crea un programa que genere un número aleatorio entre 0 y 100 y el usuario tenga que adivinarlo. Cada vez que el usuario introduzca un número el programa le dirá si el número es más alto o más bajo. Para generar un número aleatorio puedes utilizar la función randint(a, b) que devuelve un entero aleatorio entre a y b. Para poder utilizar esta función antes tienes que importar la librería con la orden from random import *

```python
from random import *
cpu = randint(0, 100)
user = int(input("introduce un numero"))
while(user != cpu):
    if user > cpu:
        print("el numero es menor ")
              else:
print("el numero es mayor ")

print("has acertado")
``



###Crea un programa que implemente el clásico juego de piedra, papel, tijeras, lagarto y spock.
Ganará el primero que gane 5 manos.

```python
from random import *

eleciones = ["piedra", "papel", "tijeras", "lagarto", "spock"]

enemigo_victorias = 0
player_victorias = 0
while(not (enemigo_victorias == 5 or player_victorias == 5)):
    player_eleccion = input("Elije piedra, papel tijeras, lagarto o spock: ")
    enemigo_eleccion = choice(eleciones)
    match (enemigo_eleccion):
        case "piedra":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "papel" or player_eleccion ==  "spock":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "tijeras" or player_eleccion ==  "lagarto":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "papel":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "tijeras" or player_eleccion ==  "lagarto":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "piedra" or player_eleccion ==  "spock":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "tijeras":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "piedra" or player_eleccion ==  "spock":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "papel" or player_eleccion ==  "lagarto":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "lagarto":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "tijeras" or player_eleccion ==  "piedra":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "papel" or player_eleccion ==  "spock":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "spock":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "papel" or player_eleccion ==  "lagarto":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "tijeras" or player_eleccion ==  "piedra":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
    print("Victorias de player " + str(player_victorias))
    print("Victorias de enemigo: " + str(enemigo_victorias))
        
if(enemigo_victorias == 5):
    print("Enemigo gana")
else:
    print("Player gana")
```






###Crea un programa que genere los primeros n números de la secuencia de Fibonacci

```python
n = int(input("introduce un numero"))
Fibo =[0, 1]
for i in range(2, n):
    continua = fibo[i-1] + fibo[i-2]   # suma de los dos anteriores
    fibo.append(continua)

print(fibo[:n])
```


###Crea un programa que solicite un número al usuario y le diga si es primo o no. Un número primo solo es divisible por 1 y por sí mismo.

```python
n =int(input("mete un numero"))

if n < 2:
    print(f"{n} NO es primo")
else:
    primo = True   
    
    for i in range(2, n):
        if n % i == 0:   
            primo = False
            break  

    if primo:
        print(f"{n} SÍ es primo")
    else:
        print(f"{n} NO es primo")
```


###calcular el factorial de un numero.

```python
num = int(input("Introduce un número entero: "))

resultado = 1
for i in range(1, num + 1):
    resultado *= i   
print(f"El factorial de {num} es {resultado}")
```


###Crea un programa que solicite al usuario una cadena de texto y muestre cuántas vocales y cuántas consonantes contiene.
```python
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

print(f"Número de vocales: {contvocales}")
print(f"Número de consonantes: {contconsonantes}")

```



###devolver una cadena invertida
```python
original = input("Introduce texto ")

vuelta = original[::-1]

print(f"La cadena invertida es: {vuelta}")
```

###Crea un programa que solicite al usuario una palabra y determine si es un palíndromo (se lee igual al derecho y al revés).

```python
palabra = input("Introduce una palabra: ")

vuelta = palabra[::-1]

if palabra == vuelta:
    print(f"La palabra '{palabra}' SÍ es un palíndromo")
else:
    print(f" La palabra '{palabra}' NO es un palíndromo")
```



#es par o impar?
```python
num = int(input("Introduce un número : "))

pares = []
impares = []

for i in range(1, num + 1):
    if i % 2 == 0:   
        pares.append(i)
    else:            
        impares.append(i)

print(f"Números pares entre 1 y {num}: {pares}")
print(f"Números impares entre 1 y {num}: {impares}")
```

###Crea un programa que pida al usuario un número entero y calcule la suma de todos sus dígitos.

```python
entero = input("Introduce un número : ")

resultado = 0

for digito in entero:
    resultado += int(digito)

print(f"La suma de los dígitos de {entero} es {resultado}")

```

###Crea un programa que pida al usuario dos números y una operación (suma, resta, multiplicación o división) y muestre el resultado.
```python
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



###Crea un programa que convierta entre grados Celsius, Fahrenheit y Kelvin. El usuario introducirá primero la cantidad y la unidad de origen, y después la unidad de destino.
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


###Crea un programa que genere una contraseña aleatoria de una longitud que indique el usuario. La contraseña debe incluir letras 
mayúsculas, minúsculas, números y símbolos especiales.

```Python

import string

longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = "".join(random.choice(caracteres) for _ in range(longitud))

# Paso 4: mostrarla
print(f"Tu contraseña generada es: {contraseña}")

```



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

