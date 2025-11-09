# sistemas de gestión empresarial

## el lenguaje Python: diccionarios.

### Crea un diccionario de frutas y precios. Permite al usuario ingresar el nombre de una fruta y muestra su precio si existe en el diccionario, o un mensaje de que no está disponible en caso contrario

```python 
buscador = input("Introduce la fruta que quieras conocer: ")

productos = {"Platano" : 3.50, "pera" : 5.89, "manzana" : 5.10}

if(buscador in productos):
    print(buscador + str(productos[buscador]))
else:
    print("No se encuentra la fruta solicitada")
```

### Suponiendo un diccionario con al siguiente estructura, crea un programa que calcule cuántas categorías hay, cuántos productos tiene cada categoría y cuántos productos hay en total

```python
productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}
print(len(productos))

for producto in productos:
    print(producto + ": " + str(len(productos.get(producto))) + " cantidad de productos")
    ```

#    ## Escribe un programa que tome una frase y use un diccionario para contar la frecuencia de cada palabra

```python
entrada = input("Introduce una frase: ")

entrada_split = entrada.split()

palabras = {}

for palabra in entrada_split:
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1

print(str(palabras))
```



###  Supón un diccionario donde cada clave es una asignatura y el valor correspondiente una lista de estudiantes matriculados, tal como se muestra en el diccionario de ejemplo. Crea un programa que tenga un menú con tres opciones:

Listar estudiantes matriculados en una asignatura
Matricular un estudiante en una asignatura
Dar de baja un estudiante de una asignatura.

```python 
asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

encontrado = False

print("1. Listar estudiantes matricula")
print("2. Matricular estudiante en una asignatura")
print("3. Dar de baja a un estudiante")

def listar_alumnos(lista):
    asignatura = input("Elige una asignatura:")
    asignatura_correcta = False
    alumnos = ""
    while not asignatura_correcta:
        if asignatura in lista:
            alumnos = str(lista[asignatura])
            asignatura_correcta = True
        else:
            asignatura = input("Elige una asignatura: ")
    return alumnos

def matricular_alumno(lista):
    asignatura = input("Elige una asignatura: ")
    alumno = input("Elije el nombre del alumno")
    asignatura_correcta = False
    while not asignatura_correcta:
        if asignatura in lista:
            asignaturas[asignatura].append(alumno)
            asignatura_correcta = True
        else:
            asignatura = input("Elige una asignatura: ")
            alumno = input("Elije el nombre del alumno")

    return alumno + " ha sido añanido a " + asignatura

def dar_de_baja(lista):
    asignatura = input("Elige una asignatura: ")
    alumno = input("Elije el nombre del alumno")
    asignatura_correcta = False
    while not asignatura_correcta:
        if asignatura in lista:
            if alumno in asignaturas[asignatura]:
                asignaturas[asignatura].remove(alumno)
                asignatura_correcta = True
            else:
                asignatura = input("Elige una asignatura: ")
                alumno = input("Elije el nombre del alumno")
        else:
            asignatura = input("Elige una asignatura: ")
            alumno = input("Elije el nombre del alumno")

    return alumno + " ha sido añanido a " + asignatura

respuesta = ""
while not encontrado:
    opcion = input("Por favor elige una opción: ")
    if opcion == "1":
        respuesta = listar_alumnos(asignaturas)
        encontrado = True
    elif opcion == "2":
        respuesta = matricular_alumno(asignaturas)
        encontrado = True
    elif opcion == "3":
        respuesta = dar_de_baja(asignaturas)
        encontrado = True
    else:
        encontrado = False


print(respuesta)
```


### 6.- Combinar dos diccionarios
Escribe un programa que tome dos diccionarios de productos y precios, y combine los productos comunes sumando sus precios, sin duplicar los elementos únicos.

```python
productos1 = {"peras" : 1, "mangos" : 2, "cocos" : 4}
productos2 = {"kiwis" : 4, "cocos" : 3, "mangos" : 2}

def combinar_diccionarios(dic1, dic2):
    combinado = dic1.copy()  
    for producto, precio in dic2.items():
        if producto in combinado:
            combinado[producto] += precio 
        else:
            combinado[producto] = precio
    return combinado

resultado = combinar_diccionarios(productos1, productos2)
print(resultado)  
```

### Escribe un programa que tome una frase y use un diccionario para contar la frecuencia de cada palabra.

```python
frase = input("introduce una frase ")

repeticiones = {}
palabras = frase.split()

for palabra in palabras:
    if palabra in repeticiones:
        repeticiones[palabra] += 1
    else:
        repeticiones[palabra] = 1

print("Frecuencia de palabras:")
for palabra, cantidad in repeticiones.items():
    print(palabra, ":", cantidad)

```



### Escribe una función que tome un diccionario y devuelva otro con las claves y valores intercambiados (lo que antes eran valores ahora son claves, y viceversa).

```python
original = {"python": 1, "java": 2, "angular": 3}
def invertir_diccionario(diccionario):
    invertido = {}
    for clave, valor in diccionario.items():
        invertido[valor] = clave
    return invertido

resultado = invertir_diccionario(original)
print(resultado)
```


#### Dado un diccionario de empleados y salarios, filtra e imprime solo los empleados con un salario mayor a un umbral definido.

```python`
empleados = {"Bruno": 1200," Carlos": 1500, "Olga": 1300, "Pedro": 1400}
umbral = int(input("establece un limite"))
def supera_umbral(umbral):
    for empleado, salario in empleados.items():
        if salario > umbral:
            return empleado, ":", salario
        
        print(supera_umbral(umbral))
```

### Partiendo de un diccionario donde las claves son nombres de departamentos y los valores, diccionarios de empleados y sus puestos, tal como se ve en el código de ejemplo, crea un programa que permita realizar las siguientes funciones:

```python 

#Mostrar el listado de todos los empleados de un departamento
#Añadir un empleado a un departamento
#Eliminar un empleado de un departamento
departamentos = {
    "Recursos Humanos": {
        "Ana": "Gerente de Recursos Humanos",
        "Luis": "Especialista en Reclutamiento",
        "Elena": "Asistente de Recursos Humanos"
    },
    "Tecnología": {
        "Carlos": "Desarrollador Backend",
        "María": "Desarrolladora Frontend",
        "Pedro": "Administrador de Sistemas"
    },
    "Marketing": {
        "Sofía": "Directora de Marketing",
        "Jorge": "Especialista en SEO",
        "Laura": "Community Manager"
    },
    "Finanzas": {
        "Juan": "Analista Financiero",
        "Lucía": "Contadora",
        "Raúl": "Asesor Financiero"
    }
}

while True:
    print(" te doy estas opciones")
    print("Mostrar empleados de un departamento")
    print(" Añadir empleado a un departamento")
    print(" Eliminar empleado de un departamento")
    print(" Salir")


    departamento = input("Introduce el nombre del departamento: ")
    opcion = input("que quieres hacer: ")
    if opcion == "mostrar":
        if departamento in departamentos:
            print(f"\nEmpleados en {departamento}:")
            for empleado, puesto in departamentos[departamento].items():
                print(f"- {empleado}: {puesto}")
        else:
            print("Departamento no encontrado")

    elif opcion == "añadir":
        departamento = input("Introduce el departamento donde agregar el empleado: ")
        if departamento in departamentos:
            nombre = input("Nombre del empleado: ")
            puesto = input("Puesto del empleado: ")
            departamentos[departamento][nombre] = puesto
            print(f"Empleado {nombre} añadido a {departamento}.")
        else:
            print("Departamento no encontrado")

    elif opcion == "eliminar":
        departamento = input("Introduce el departamento: ")
        if departamento in departamentos:
            nombre = input("Empleado a eliminar: ")
            if nombre in departamentos[departamento]:
                del departamentos[departamento][nombre]
                print(f"Empleado {nombre} eliminado de {departamento}.")
            else:
                print("El empleado no existe en ese departamento")
        else:
            print("Departamento no encontrado")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")
````

