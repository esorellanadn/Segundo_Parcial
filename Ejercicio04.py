"""Crea un programa que permita realizar operaciones matemáticas
básicas (suma, resta, multiplicación y división) utilizando funciones modulares para cada
operación."""

operacion = int(input("Ingrese el número según corresponda con la operación que desea hacer, Suma: 1, Resta: 2, Multiplicación: 3, División: 4 ")) #El usuario elige la operación que desea hacer
num1 = int(input("Ingrese un número: ")) #Ingreso de datos
num2 = int(input("Ingrese un número: ")) #Ingreso de datos

def suma(num1, num2): #Función suma
    suma = (num1 + num2)
    return (suma)

def resta(num1, num2): #Función resta
    resta = (num1 - num2)
    return (resta)

def mult(num1, num2): #Función multiplicación
    mult = (num1 * num2)
    return (mult)

def div(num1, num2): #Función división
    div = (num1 / num2)            
    retunr (div)

if operacion == 1: #Si el usuario oprime 1, hace una suma
	resulsuma= suma (num1, num2)
	print("Resultado: ", resulsuma)

elif operacion == 2: #Si el usuario oprime 2, hace una resta
	resulresta= resta (num1, num2)
	print("Resultado: ", resulesta)

elif operacion == 3: #Si el usuario oprime 3, hace una multiplicación
	resulmult= mult (num1, num2)
	print("Resultado: ", resulmult)

elif operacion == 4: #Si el usuario oprime 4, hace una división
	Division_es= div (num1, num2)
	print("Resultado: ", resuldiv)