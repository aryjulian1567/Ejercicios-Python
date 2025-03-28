print("Ingrese un tres numeros")
num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero:"))
num3 = int(input("Ingrese el tercer numero:"))

if num1 >= num2 and num1 >= num3:
    print ("El numero mayor es el primer numero:",num1)
elif num2>= num1 and num2 >= num3:
    print ("El numero mayor es el segundo numero:", num2)
else:
    print ("El numero mayor es el tercer numero:", num3)
    
                    
