#Escribe un programa que transforme una cadena de palabras separadas por espacios o guiones en formato camelCase (la primera letra de cada palabra, excepto la primera, debe ser mayúscula y no debe haber espacios ni guiones).

original = input("escribe un texto:")

original = original.replace("-", " ")

palabras = original.split()

if len(palabras) > 0:
    conversion = palabras[0].lower() + "".join(p.capitalize() for p in palabras[1:])
else:
    conversion = ""

print( conversion)
