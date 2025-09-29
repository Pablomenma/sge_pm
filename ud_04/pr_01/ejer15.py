#es par o impar?
num = int(input("Introduce un número : "))

pares = []
impares = []

for i in range(1, num + 1):
    if i % 2 == 0:   
        pares.append(i)
    else:            
        impares.append(i)

print(f"Números pares entre 1 y {num}: {pares}")
print(f"Números impares entre 1 y {num}: {impares}")
