#Escribe un programa que convierta las letras minúsculas de una cadena en mayúsculas y viceversa.

texto = input("Escribe un texto: ")
texto = input("Escribe una cadena: ")
resultado = ""

for letra in texto:
    if letra.islower():          
        resultado += letra.upper()
    elif letra.isupper():        
        resultado += letra.lower()
    else:
        resultado += letra       

print("La cadena convertida es:", resultado)


