def func_max(x,y):
    if x > y:
        resultado = x
        print("El número mayor es: " + resultado)
    elif x < y:
        resultado = y
        print("El número mayor es: " + resultado)
    else:
        print("Son iguales")


d1 = input("Ingresa un número: ")
d2 =input("Ingresa otro número: ")

func_max(d1,d2)