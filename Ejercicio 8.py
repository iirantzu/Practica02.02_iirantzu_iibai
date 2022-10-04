#Escribir un programa que pida al usuario dos números enteros y muestre
#por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde
#<n> y <m> son los números introducidos por el usuario, y <c> y <r> son
#el cociente y el resto de la división entera respectivamente.

entero1 = int(input("Introduce el numero entero 1: "))
entero2 = int(input("Introduce el numero entero 2: "))
coef = ((entero1) // (entero2))
resto = ((entero1) % (entero2))
print("El coeficiente es " + str(coef) + " y el resto es " + str(resto))
