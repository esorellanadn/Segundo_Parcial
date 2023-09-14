"""Crear un programa que permita convertir
entre Celsius y Fahrenheit. Crear dos funciones modulares: una para convertir de Celsius a
Fahrenheit y otra para convertir de Fahrenheit a Celsius."""

conv = int(input("Si desea convertir de Celsius a Fahrenheit presione 0, si desea convertir de Fahrenheit a Celsius presione 1: ")) #El usuario elige que tipo de conversión desea hacer
temp = int(input("Ingrese el número que desea convertir: ")) #El usuario ingresa la temperatura

def celtofahr (temp): #Modulo de Celsius a Fahrenheit
       celtofahrorop = (temp * 9/5) + 32 #La operación que permite la conversión
       return celtofahrorop

def fahrtocel (temp): #Modulo de Fahrenheit a Celsius
       fahrtocelop = (temp - 32) * 5/9 #La operación que permite la conversión
       return fahrtocelop

if conv == 0: #Si el usuario presiona 0 convertira de C° a F°
    resultado = celtofahr (temp)
    print ("El resultado es: ", resultado) 

elif conv == 1: #Si el usuario presiona 1 convertira de F° a C°
    resultado = fahrtocel (temp)
    print ("El resultado es: ", resultado)