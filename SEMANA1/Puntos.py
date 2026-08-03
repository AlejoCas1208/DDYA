def signo(numero):
    
    if numero > 0:
        print("Es positivo")

    if numero == 0:
        print("Cero")

    if numero < 0:
        print("Es negativo")

def pareimpar(numero):
    
    if numero % 2 == 0:
        print("El numero",numero,"Es par")

    if numero % 2 != 0:
        print("El numero",numero,"Es impar ")

def fibonacci(numero):
    
    a = 0
    b = 1

    while a < numero:
        c = a + b
        a = b
        b = c

    if a == numero:
        print("Pertenece a Fibonacci")

    if a != numero:
        print("No pertenece a Fibonacci")

def primo(numero):
    
    vc = 0
    i = 1

    while i <= numero:
        
        if numero % i == 0:
            vc = vc + 1
        i = i + 1

    if vc == 2:
        print("Es primo")

    if vc != 2:
        print("No es primo")

def sumar_intermedios(a, b):
    
    sum = 0
    i = a

    while i <= b:
        sum = sum + i
        i = i + 1

    print("La suma es:", sum)

def potencia(numero):
    
    if numero % 2 == 0:

        print("Como es par entonces",numero ** 3)

    if numero % 2 != 0:

        print("Como es impar entonces",numero ** 2)

def vocales_consonantes(mes):
    
    i = 0

    while i < len(mes):

        if mes[i] == "a":

            print(mes[i], " Es Vocal")

        if mes[i] == "e":

            print(mes[i], "Es Vocal")

        if mes[i] == "i":

            print(mes[i], "Es Vocal")

        if mes[i] == "o":

            print(mes[i], "Es Vocal")

        if mes[i] == "u":

            print(mes[i], "Es Vocal")

        if mes[i] != "a" and mes[i] != "e" and mes[i] != "i" and mes[i] != "o" and mes[i] != "u":

            print(mes[i], "Es Consonante")

        i = i + 1

def main():
    
    numero = int(input("Ingrese un número: "))

    signo(numero)
    pareimpar(numero)
    fibonacci(numero)
    primo(numero)
    potencia(numero)

    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    sumar_intermedios(a, b)
    mes = input("Ingrese Mes: ")
    vocales_consonantes(mes)


main()