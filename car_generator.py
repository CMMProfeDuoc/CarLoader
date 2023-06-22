from file_loader import *
import random
from random import randint

colores = ["Rojo","Verde","Azul","Amarillo","Morado","Negro","Blanco","Burdeo"]
carFiles = [["Ferrari"],["Honda"],["Toyota"],["Mitsubishi"]]

carCount = 100
random.seed()

for car in carFiles:
	lista = load_file(car[0])
	for l in lista:
		car.append(l)

print(carFiles[2])


