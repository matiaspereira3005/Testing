def func_max(x,y,z):
    if x < y:
        if y < z:
            resultado = z
            print("El número mayor es: " + str(resultado))
        else:
            resultado = y
            print("El número mayor es: " + str(resultado))
    elif y < x:
        if x < z:
            resultado = z
            print("El número mayor es: " + str(resultado))
        else:
            resultado = x
            print("El número mayor es: " + str(resultado))
    elif x < z:
        if z < y:
            resultado = y
            print("El número mayor es: " + str(resultado))
        else:
            resultado = z
            print("El número mayor es: " + str(resultado))

    else:
        print("Son iguales")


d1 = int(input("Ingresa un número: "))
d2 = int(input("Ingresa otro número: "))
d3 = int(input("Ingresa otro número: "))

func_max(d1,d2,d3)