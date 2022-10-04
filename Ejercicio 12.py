#Una panadería vende barras de pan a 3.49€ cada una. El pan que no
#es el día tiene un descuento del 60%. Escribir un programa que
#comience leyendo el número de barras vendidas que no son del día.
#Después el programa debe mostrar el precio habitual de una barra
#de pan, el descuento que se le hace por no ser fresca y el coste
#final total.

pan =int(input("Introduce el número de panes vendidas queno son frescas: "))
precio = 3.49
descuento = 0.6
coste_de_pan_viejo = precio * (1 - descuento)
coste = pan * precio * (1 - descuento)
print("El coste de un pan fresca es " + str(precio) + "€")
print("El descuento sobre un pan no fresca es " + str(round(coste_de_pan_viejo, 2)) + "€")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")