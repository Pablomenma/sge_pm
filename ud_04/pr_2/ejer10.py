#Escribe un programa que elimine todos los caracteres no alfanuméricos (como signos de puntuación) de una cadena.
texto = input("introduce un texto")
salida = ""

for c in texto:

    if c.isalnum():

        salida += c
 
print(salida)
 