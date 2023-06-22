from file_loader import *
import random
from random import randint

maxCarCount = 10

colores = ["Rojo","Verde","Azul","Amarillo","Morado","Negro","Blanco","Burdeo"]
carFiles = [["Ferrari"],["Honda"],["Toyota"],["Mitsubishi"]]

patentes = generador_patentes(maxCarCount)

autos = []

random.seed()

for car in carFiles:
	lista = load_file(car[0])
	for l in lista:
		car.append(l)

#print("TEST",carFiles[0][1][1])

for pat in patentes:
	m = randint(0,len(carFiles)-1)
	marca = carFiles[m][0]
	n = randint(1,len(carFiles[m])-1)
	modelo = carFiles[m][n][0]

	año = randint(int(carFiles[m][n][1]),int(carFiles[m][n][2]))

	color = colores[randint(0,len(colores)-1)]

	#print(marca,modelo,año,pat,color)

	autos.append({"marca":marca,"modelo":modelo,"año":año,"patente":patente,"color":color})

print(autos)
