#Crea un programa que genere un número aleatorio entre 0 y 100 y el usuario tenga que adivinarlo. Cada vez que el usuario introduzca un número el programa le dirá si el número es más alto o más bajo.
#Para generar un número aleatorio puedes utilizar la función randint(a, b) que devuelve un entero aleatorio entre a y b. Para poder utilizar esta función antes tienes que importar la librería con la orden from random import *
from random import *
cpu = randint(0, 100)
user = int(input("introduce un numero"))
while(user != cpu):
    if user > cpu:
        print("el numero es menor ")
              else:
print("el numero es mayor ")

print("has acertado")