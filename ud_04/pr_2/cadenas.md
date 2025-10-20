# PRÁCTICAS SISTEMAS DE GESTIÓN EMPRESARIAL. PABLO MENDOZA MAYO

## Unidad 04: Python

### Cadenas en Python pr2

#### Escribe una función que reciba una cadena y cuente cuántas vocales y consonantes contiene

```python
def contar_vocales_consonantes(texto):
    texto = texto.lower()
    
    vocales = "aeiou"
    contvocal = 0
    contconsonante = 0
    
    for caracter in texto:
        if caracter.isalpha():  # Solo contamos letras (ignoramos espacios, números, signos)
            if caracter in vocales:
                contvocal += 1
            else:
                contconsonante += 1
    
    return contvocal, contconsonante

v, c = contar_vocales_consonantes(texto)
print(f"Vocales: {v}, Consonantes: {c}")

```

#### invertir una cadena

```python
cadena  = input("introduce un texto")
reves = cadena[::-1]
print(reves)

```

#### Crea una función que cuente cuántas palabras hay en una cadena, suponiendo que las palabras están separadas por espacios

```python
cadena = input("Introduce la cadena: ")
def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)



print("Número de palabras:", contar_palabras(texto))

```

#### Escribe una función que elimine los caracteres duplicados en una cadena, manteniendo solo la primera aparición de cada uno

```python
texto = input("Escribe un texto: ")
def eliminar(texto):
    salida = ""   
    for letra in texto:
        if letra not in salida:   
            salida += letra
    return salida

# Ejemplo de uso
print("Texto sin duplicados:", eliminar(texto))
```

#### Escribe un programa que convierta las letras minúsculas de una cadena en mayúsculas y viceversa

```python
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



```

#### Escribe una función que rote una cadena hacia la izquierda un número dado de veces

```python
def rotatexto(texto, n):
    n = n % len(texto)
    return texto[n:] + texto[:n]

texto = input("Escribe un texto: ")
veces = int(input("¿Cuántas veces quieres rotarla a la izquierda?: "))

resultado = rotatexto(texto, veces)
print("La cadena rotada es:", resultado)
```

### Crea un programa que verifique si dos cadenas son anagramas. Se considera que dos palabras son anagramas si tienen las mismas letras en diferente orden por e

```python
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

if sorted(palabra1) == sorted(palabra2):
    print("Las palabras son anagramas")
else:
    print("Las palabras no son anagramas"
    ``
    
    #### Escribe un programa que elimine todos los caracteres no alfanuméricos (como signos de puntuación) de una cadena

    ```python
texto = input("introduce un texto")
salida = ""

for c in texto:

    if c.isalnum():

        salida += c
 
print(salida)
 ```

 #### Escribe un programa que transforme una cadena de palabras separadas por espacios o guiones en formato camelCase (la primera letra de cada palabra, excepto la primera, debe ser mayúscula y no debe haber espacios ni guiones)

```python
original = input("escribe un texto:")

original = original.replace("-", " ")

palabras = original.split()

if len(palabras) > 0:
    conversion = palabras[0].lower() + "".join(p.capitalize() for p in palabras[1:])
else:
    conversion = ""

print( conversion)

```

#### Escribe una función que implemente la codificación por longitud de ejecución (RLE), que consiste en comprimir una cadena representando las secuencias consecutivas de caracteres iguales con el carácter seguido de la cantidad de repeticiones

```python
cadena="aaabbbcdeeeaa"
 
prev = ""

count = 0

res = ""
 
for c in cadena:

    if prev == c:

        count += 1

    else:

        if prev:

            res = res + prev

            res = res + str(count)

        prev = c

        count = 1

res = res + prev

res = res + str(count)

print(res)
 ```

#### Crea una función que decodifique una cadena que ha sido comprimida usando el método RLE

 ```python
texto_codificado = input("Escribe una cadena codificada en RLE : ")
def decodificar_rle(texto):
    descifrado = ""
    numero = ""

    for letra in texto:
        if letra.isdigit():
            numero += letra
        else:
            descifrado += letra * int(numero)
            numero = ""  # Reiniciamos el número

    return descifrado


texto_decodificado = decodificar_rle(texto_codificado)
print("Cadena decodificada:", texto_decodificado)

```

#### Escribe una función que compare dos cadenas sumando el valor ASCII de cada carácter y devuelva cuál tiene un mayor valor total. Para este ejercicio ten en cuenta que la función integrada ord() devuelve el valor ASCII de un carácter

```python`
texto1 = input("Escribe la primera cadena: ")
def comparar_cadenas_ascii(cadena1, cadena2):
    suma1 = sum(ord(c) for c in cadena1)
    suma2 = sum(ord(c) for c in cadena2)

    print(f"Valor total de '{cadena1}': {suma1}")
    print(f"Valor total de '{cadena2}': {suma2}")

    if suma1 > suma2:
        return f"La cadena con mayor valor ASCII es: '{cadena1}'"
    elif suma2 > suma1:
        return f"La cadena con mayor valor ASCII es: '{cadena2}'"
    else:
        return "Ambas cadenas tienen el mismo valor total ASCII."

texto2 = input("Escribe la segunda cadena: ")

resultado = comparar_cadenas_ascii(texto1, texto2)
print(resultado)
```

#### Escribe un programa que reciba una cadena y devuelva la longitud de la palabra más larga

```python
texto = input("Escribe una frase: ")

palabras = texto.split()

if len(palabras) > 0:
    palabra_mas_larga = max(palabras, key=len)
    longitud = len(palabra_mas_larga)

    print("La palabra más larga es:", palabra_mas_larga)
    print("Su longitud es:", longitud)
else:
    print("No se ingresaron palabras.")

```

#### Escribe una función que tome un número de forma de cadena y le agregue separadores de miles


```python
def poner_puntos(cadena):
    contador = len(cadena)
    cadena_traducida = ""
    for i in range(len(cadena)):
        if(contador % 3 == 0):
            cadena_traducida += "."
        cadena_traducida += cadena[i]
        contador -= 1
    return cadena_traducida

print(poner_puntos(entrada))
```
