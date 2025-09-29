#Crea un programa que solicite un número n y un valor k y que muestre por la terminal los primeros k elementos de la tabla de multiplicar de n.
n = int( input("Dime el valor n: ") )

k = int( input("Dime el valor k: ") )

for iter in range(1, k+1):

    print( f"{n} * {iter} = { n*iter }" )
 

