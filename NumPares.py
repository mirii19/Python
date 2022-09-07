n1 = int(input("Escriba un primer número")) # Funcion input podremos leer lo que el usuario introduzca por teclado
n2 = int(input("Escriba un segundo número"))

def RecorrerNumeros(n1, n2):
    if n1 > n2:
        mayor = n1
        menor = n2
    else:
        mayor = n2
        menor = n1
    
    while menor <= mayor:
        print(menor)
        menor = menor+1

        if (menor % 2 ==0):
            print("El número {} es un numero par".format(menor))

RecorrerNumeros(n1,n2)