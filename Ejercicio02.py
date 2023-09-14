"""Escribe un programa que encuentre y
muestre todos los números primos dentro de un rango dado. Utiliza una función modular
para determinar si un número es primo."""

def calc (num): #Modulo para determinar si el número es primo
    cont = 0 #Contador para que el usuario vaya ingresando los números
    for div in range (1, num + 1):
        if num % div == 0: #División MOD
            cont += 1
            
    if cont == 2: #Si el número tiene dos divisores positivos es primo
        return "Primo"
    else: 
        return "Compuesto" #Si el número no es primo es compuesto

intento = 1
while intento == 1: #Mientras intento sea igual a 1 el usuario seguira ingresando números
    num = int(input("Ingrese un número: "))
    resultado = calc (num)
    print("Números primos:", resultado)
    intento = int(input("Si desea seguir ingresando números presione 1 sino presione 0: "))