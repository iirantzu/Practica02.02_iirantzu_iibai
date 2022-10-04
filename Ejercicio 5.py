#Escribir un programa que pregunte al usuario por el número de
# horas trabajadas y el coste por hora. Después debe mostrar
# por pantalla la paga que le corresponde.

Horas = float(input("Introduce tus horas de trabajo: "))
Coste = float(input("Introduce lo que cobras por hora: "))
Paga = round(Horas * Coste, 3)
print("Tu Paga es " + str(Paga) + "€")