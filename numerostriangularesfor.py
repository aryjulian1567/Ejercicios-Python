N = int(input("Ingresa la cantidad de numeros triangulares para imprimir:"))
for n in range(1, N + 1):
    triangular = n * (n+1) // 2 
    print (triangular)
