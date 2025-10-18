#Crea un programa que convierta entre diferentes unidades de longitud (milímetros, centímetros, metros y kilómetros). El usuario introducirá primero la cantidad, luego la unidad de medida en que está y finalmente la unidad de medida a la que se va a convertir.
cantidad = float(input("escribe una cantidad"))
```python
cantidad = int(input("introduce la unidad a la que quieres cambiar"))
unidad_inicial = input("Introduce la unidad de miedida inicial")
unidad_final = input("Introduce la unidad de medida final")

match unidad_final:
    case "mm":
        cantidad = (
            (cantidad * (10 ** 1)) if unidad_inicial == "cm" else
            (cantidad * (10 ** 3)) if unidad_inicial == "m" else
            (cantidad * (10 ** 6)) if unidad_inicial == "km" else
            cantidad
        )
    case "cm":
        cantidad = (
            (cantidad * (10 ** -1)) if unidad_inicial == "mm" else
            (cantidad * (10 ** 2)) if unidad_inicial == "m" else
            (cantidad * (10 ** 5)) if unidad_inicial == "km" else
            cantidad
        )
    case "m":
        cantidad = (
            (cantidad * (10 ** -2)) if unidad_inicial == "cm" else
            (cantidad * (10 ** -3)) if unidad_inicial == "mm" else
            (cantidad * (10 ** 3)) if unidad_inicial == "km" else
            cantidad
        )
    case "km":
        cantidad = (
            (cantidad * (10 ** -5)) if unidad_inicial == "cm" else
            (cantidad * (10 ** -3)) if unidad_inicial == "m" else
            (cantidad * (10 ** -6)) if unidad_inicial == "mm" else
            cantidad
        )

cantidad = round(cantidad)

print("Tu medida es: " + str(cantidad) + str(unidad_final))

