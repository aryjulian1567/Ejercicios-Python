N = int(input("Ingresa la cantidad de numeros triangulares para imprimir:"))
n = 1 
triangular = 0 
while n <= N:
    triangular = n * (n+1) // 2 
    print (triangular)
    n += 1 