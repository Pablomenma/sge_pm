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


8.- Intersección de conjuntos
Dadas dos listas de números, usa filter para obtener una lista de los elementos que están en ambas listas (sin usar conjuntos).

# Ejemplo de listas de entrada
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
# Resultado esperado: [3, 4, 5]
9.- Agrupación de palabras por longitud
Dada una lista de palabras, crea un diccionario donde la clave es la longitud de la palabra y el valor es una lista de palabras de esa longitud. Usa map y filter.

# Ejemplo de lista de entrada
palabras = ["sol", "luna", "estrella", "cielo", "mar"]
# Resultado esperado: {3: ['sol', 'mar'], 4: ['luna', 'cielo'], 8: ['estrella']}
10.- Concatenación de listas de caracteres
Dadas dos listas de caracteres, usa reduce para concatenarlas en una sola lista sin utilizar + o métodos de concatenación.

# Ejemplo de listas de entrada
lista1 = ['a', 'b', 'c']
lista2 = ['x', 'y', 'z']
# Resultado esperado: ['a', 'b', 'c', 'x', 'y', 'z']
11.- Calificación de alumnos
Dada una lista de tuplas con el nombre del alumno y su calificación, utiliza map y filter para obtener una lista con los nombres de los alumnos que han aprobado (nota >= 5).

# Ejemplo de lista de entrada
alumnos = [("Ana", 4), ("Bruno", 7), ("Clara", 5), ("David", 8)]
# Resultado esperado: ['Bruno', 'Clara', 'David']
12.- Calcular producto cartesiano
Dadas dos listas de números, usa map para obtener el producto cartesiano de ambas listas, devolviendo una lista de tuplas.

# Ejemplo de listas de entrada
lista1 = [1, 2]
lista2 = [3, 4]
# Resultado esperado: [(1, 3), (1, 4), (2, 3), (2, 4)]
13.- Pipe de transformaciones de listas
Implementa una función que tome una lista de funciones y una lista de números, y aplique cada función de la lista en secuencia sobre la lista de números usando reduce.

# Ejemplo de funciones y lista de entrada
funciones = [lambda x: x*2, lambda x: x+3, lambda x: x-1]
numeros = [1, 2, 3]
# Resultado esperado: [((1*2)+3)-1, ((2*2)+3)-1, ((3*2)+3)-1] -> [4, 6, 8]
14.- Aplicar operaciones de cadena
Dada una lista de cadenas, usa map y filter para crear una nueva lista con las cadenas que tengan más de tres letras y en las que todas las letras sean mayúsculas. Además, convierte el primer carácter en minúscula.

# Ejemplo de lista de entrada
palabras = ["HOLA", "MUNDO", "SOL", "CIELO", "mar"]
# Resultado esperado: ['hOLA', 'mUNDO', 'cIELO']