num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
op=str(input("Seleccione operador (+, -, *, /): "))
match op:
    case ("+"):
        print (num1+num2)
    case ("-"):
        print (num1-num2)
    case ("*"):
        print (num1*num2)
    case ("/"):
        if (num2 or num1 != 0):
            print ("Error: Division por cero D:")
        else:
            print (num1/num2)
    case _:
        print ("operacion invalida")