n = int (input("Ingrese un numero:"))
factorial = 1
i = 1 
while i <= n:
    factorial *= i 
    i += 1
print ("El factorial de ", n, "es: ", factorial)    