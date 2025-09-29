#Crea un programa que solicite al usuario una palabra y determine si es un palíndromo (se lee igual al derecho y al revés).
palabra = input("Introduce una palabra: ")

vuelta = palabra[::-1]

if palabra == vuelta:
    print(f"La palabra '{palabra}' SÍ es un palíndromo")
else:
    print(f" La palabra '{palabra}' NO es un palíndromo")
