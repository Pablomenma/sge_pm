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


