#Crea un programa que genere una contraseña aleatoria de una longitud que indique el usuario. La contraseña debe incluir letras mayúsculas, minúsculas, números y símbolos especiales.
import random
import string

longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = "".join(random.choice(caracteres) for _ in range(longitud))

# Paso 4: mostrarla
print(f"Tu contraseña generada es: {contraseña}")
