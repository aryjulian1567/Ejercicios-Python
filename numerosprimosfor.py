n = 2 
primos = []
for _ in range (100):
    numeroprimo = True
    for i in range (2, n):
        if n % i == 0:
            numeroprimo = False
            break
    if numeroprimo :
        primos += [n]
    if len(primos) == 20:
        break
    n += 1
print (primos)
