"""Escribe un programa que realice una búsqueda de un número
dado, en un arreglo. Crea una función modular para llevar a cabo la búsqueda."""

tope = True
arreglo = [12, 22, 777, 32, 92]
num = int(input("Ingrese un numero: ")) #Ingreso de datos

def searcharr(numero):
    search = (arreglo)
    return(search)

while tope == 0: #Mientras el tope sea igual a 1 se va a repetir
    for i in range(tope):
        arreglo.append(num) #Agregamos un numero al arreglo

    num = int(input("Ingrese un número:  ")) #Ingreso de datos
    basta = int(input("Si desea seguir ingresando números presione 0 sino presione 1")) #Opción de continuar ingresando para el usuario

if tope == 1: 
    search =int(input("Ingrese el número que desea buscar: ")) #Ingreso de datos
    search = searcharr (num)
    print("El valor se encuentra en: ", search)