def sum(lista):
    for j in lista:
        total =+ j

        return total

def mult(lista):
    for j in lista:
        total = 1
        total = total * j

        return total

lista = []
n1 = int(input("ingresa un número: "))
n2 = int(input("ingresa otro número: "))
n3 = int(input("ingresa otro número: "))
n4 = int(input("ingresa otro número: "))

lista.append(n1)
lista.append(n2)
lista.append(n3)
lista.append(n4)

print("de la suma, " + str(sum(lista)))
print("de la multiplicacion, " + str(mult(lista)))