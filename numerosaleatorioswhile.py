numeros = [9, 14, 8, 71, 23, 25, 80, 99, 33]
print ("Numeros aleatorios:", numeros)
mayor = numeros [0]
i = 1
while i < len(numeros):
    if numeros [i] > mayor:
        mayor = numeros [i]
    i += 1
print ("El numero mayor es:", mayor)