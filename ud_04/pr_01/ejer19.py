#Crea un programa que genere una contraseña aleatoria de una longitud que indique el usuario. La contraseña debe incluir letras mayúsculas, minúsculas, números y símbolos especiales.
import random
import string

# Paso 1: pedir la longitud de la contraseña
longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))

# Paso 2: definir los caracteres posibles
caracteres = string.ascii_letters + string.digits + string.punctuation

# Paso 3: generar la contraseña
contraseña = "".join(random.choice(caracteres) for _ in range(longitud))

# Paso 4: mostrarla
print(f"Tu contraseña generada es: {contraseña}")
