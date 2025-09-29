#Crea un programa que solicite un número al usuario y le diga si es primo o no. Un número primo solo es divisible por 1 y por sí mismo.
n =int(input("mete un numero"))

if n < 2:
    print(f"{n} NO es primo")
else:
    primo = True   
    
    for i in range(2, n):
        if n % i == 0:   
            primo = False
            break  

    if primo:
        print(f"{n} SÍ es primo")
    else:
        print(f"{n} NO es primo")
