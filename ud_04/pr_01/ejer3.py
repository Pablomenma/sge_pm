#Crea un programa que solicite un número al usuario y dibuje un triángulo con asteriscos cuya base sea el número introducido.
base = int(input("Introduce un número : "))

for i in range(1, base + 1):
    print("*" * i)
