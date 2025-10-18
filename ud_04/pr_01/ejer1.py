#Crea un programa que solicite un número por pantalla al usuario y siga pidiéndolo hasta que el usuario introduzca un número válido.
entrada = input("Introduce un numero: ")

while(not entrada.isdigit()):
    entrada = input("Introduce un numero: ")

print("Has introducido un numero")