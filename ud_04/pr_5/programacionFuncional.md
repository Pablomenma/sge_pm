# Sistemas de Gestion Empresarialpython

## ejercicios python: la programación funcional 

###  Filtrado de una lista de números
Usa filter para obtener solo los números pares de una lista de enteros.


```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def es_par(x):

    return x%2 == 0
 
numeros_pares = list( filter(es_par, numeros) )
 
print(numeros_pares)
 
 ```

###  Mapeo de temperaturas
Dada una lista de temperaturas en Celsius, usa map para convertirlas a Fahrenheit.

```python
celsius = [0, 20, 37, 100]
Fahrenheit = list(map(lambda c: 9/5))
print(Fahrenheit)
```

### Suma acumulativa
Utiliza reduce para obtener la suma acumulativa de una lista de números.


```python
from functools import reduce
numeros = [1, 2, 3, 4, 5]

def acumulativa(x, y):

    return x+ y 

acumulado = reduce(acumulativa, numeros)
print(acumulado)
```


### Palabras con cierta longitud
Dada una lista de palabras, usa filter para encontrar las que tienen más de cinco letras y luego map para convertirlas en mayúsculas.

```python
palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
def contiene_cinco(x):

    return len(x)< 5
def mayusculas (x):

    return x.upper


cinco_letras = list( filter(contiene_cinco, palabras) )
Alteradas = list(map(mayusculas, cinco_letras ))
print(Alteradas)
```


###  Multiplicación de pares
Dada una lista de números, utiliza filter, map y reduce para obtener el producto de los números pares.

```python 
from functools import reduce
numeros = [1, 2, 3, 4, 5, 6]
def es_par(x):

    return x%2 == 0
 
numeros_pares = list( filter(es_par, numeros) )
producto = reduce(lambda x, y: x *y, numeros_pares)
print(producto)
``

### Combinar operaciones en listas anidadas
Dada una lista de listas de enteros, usa map, filter, y reduce para obtener la suma de todos los números positivos.

```python
from functools import reduce
 
numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]
 
lista =  reduce( lambda acum, valor: acum + valor, numeros, [] )

positivos = filter( lambda num: num>0, lista )

res = reduce( lambda acum, positivo: acum + positivo, positivos, 0 )

print(res)
 
 ```
 
7.- Frecuencia de palabras
Dado un texto, crea una función que use map y reduce para obtener la frecuencia de cada palabra. Ignora las mayúsculas y minúsculas y supón que no hay símbolos de puntuación.

```python 
from functools import reduce

texto = input("escribe una frase")
def Frecuencia_palabra(frase):
    Frase_minusculas = frase.lower().split()

    mapped = map(lambda w: (w, 1), Frase_minusculas)

    def reducer(contadores, palabra):
        word, count = palabra
        if word in contadores:
            contadores[word] += count
        else:
            contadores[word] = count
        return contadores

    return reduce(reducer, mapped, {})


print(Frecuencia_palabra(texto))

```


### Intersección de conjuntos
Dadas dos listas de números, usa filter para obtener una lista de los elementos que están en ambas listas (sin usar conjuntos).

```python
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

def compartimos_numero(x):
    return x in lista2

resultado = list(filter(compartimos_numero, lista1))
print(resultado)
```

###  Agrupación de palabras por longitud
Dada una lista de palabras, crea un diccionario donde la clave es la longitud de la palabra y el valor es una lista de palabras de esa longitud. Usa map y filter.

```python 
palabras = ["sol", "luna", "estrella", "cielo", "mar"]
longitudes = list(map(len, palabras))
longitudes_unicas = []
for l in longitudes:
    if l not in longitudes_unicas:
        longitudes_unicas.append(l)


resultado = { 
    longitud: list(filter(lambda palabra: len(palabra) == longitud, palabras))
    for longitud in longitudes_unicas
}

print(resultado)

```


10.- Concatenación de listas de caracteres
Dadas dos listas de caracteres, usa reduce para concatenarlas en una sola lista sin utilizar + o métodos de concatenación.

```python
lista1 = ['a', 'b', 'c']
lista2 = ['x', 'y', 'z']
# Resultado esperado: ['a', 'b', 'c', 'x', 'y', 'z']
```

### Calificación de alumnos
Dada una lista de tuplas con el nombre del alumno y su calificación, utiliza map y filter para obtener una lista con los nombres de los alumnos que han aprobado (nota >= 5).

```python

alumnos = [("Ana", 4), ("Bruno", 7), ("Clara", 5), ("David", 8)]
aprobados = filter(lambda alumno: alumno[1] >= 5, alumnos)

nom_aprobado = list(map(lambda alumno: alumno[0], aprobados))

```



### Aplicar operaciones de cadena
Dada una lista de cadenas, usa map y filter para crear una nueva lista con las cadenas que tengan más de tres letras y en las que todas las letras sean mayúsculas. Además, convierte el primer carácter en minúscula.


```python
palabras = ["HOLA", "MUNDO", "SOL", "CIELO", "mar"]
def mas_de_tres(x):
    return len(x)> 5

def mayusculas (x):

    return x[0].lower() + x[1:].upper()


cinco_letras = list( filter(mas_de_tres, palabras) )
Alteradas = list(map(mayusculas, cinco_letras ))
print(Alteradas)
# Resultado esperado: ['hOLA', 'mUNDO', 'cIELO']
palabras = ["HOLA", "MUNDO", "SOL", "CIELO", "mar"]


```

###Dadas dos listas de caracteres, usa reduce para concatenarlas en una sola lista sin utilizar + o métodos de concatenación.

```python
from functools import reduce
lista1 = ['a', 'b', 'c']
lista2 = ['x', 'y', 'z']


def agregar(acc, val):
    acc.append(val)
    return acc

resultado = reduce(agregar, lista2, lista1.copy())

print(resultado)

```