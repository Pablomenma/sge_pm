#Crea un programa que genere los primeros n números de la secuencia de Fibonacci
n = int(input("introduce un numero"))
Fibo =[0, 1]
for i in range(2, n):
    continua = fibo[i-1] + fibo[i-2]   # suma de los dos anteriores
    fibo.append(continua)

print(fibo[:n])
