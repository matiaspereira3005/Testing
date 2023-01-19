def leng(x):
    cont = 0
    for i in x:
        cont+=1
    return cont

frase = input("ingrese un texto: ")

print("el total de letras es de: " + str(leng(frase)))