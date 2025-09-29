
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
