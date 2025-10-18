#Escribe un programa que verifique si una cadena es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).
cadena = input(" es palindromo?")
cadena = cadena.replace(" ", "").lower()

invertida= cadena[::-1]
if cadena == invertida:
    print("es palindromo")
else:
    print("no es palindromo")
