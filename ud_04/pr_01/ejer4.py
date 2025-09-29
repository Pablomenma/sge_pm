# Modifica el programa anterior para que en lugar de crear un triángulo cree una pirámide. Si el usuario introduce un número par se lo volverá a pedir hasta que introduzca un número impar.
base = int(input("Introduce un número impar: "))
while base % 2 == 0:   
    base = int(input("El número debe ser impar, inténtalo de nuevo: "))

lineas = base // 2 + 1   
for i in range(lineas):
    espacios = " " * (lineas - i - 1)         
    asteriscos = "*" * (2 * i + 1)           
    print(espacios + asteriscos)
