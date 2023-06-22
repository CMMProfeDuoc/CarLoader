from file_loader import *
import random
from random import randint

colores = ["Rojo","Verde","Azul","Amarillo","Morado","Negro","Blanco","Burdeo"]
carFiles = [["Ferrari"],["Honda"],["Toyota"],["Mitsubishi"]]

for car in carFiles:
	lista = load_file(car[0])
	for l in lista:
		car.append(l)

#poco eficaz, pero más visible
files = []
files.append(["Autos1",20])
files.append(["Autos2",18])
files.append(["Autos3",25])
files.append(["AutosBIG1",100])
files.append(["AutosBIG2",150])
files.append(["AutosTEST1",100])
files.append(["AutosTEST2",200])


for f in files:
	patentes = generador_patentes(f[1])
	autos = []
	random.seed()
	#print("TEST",carFiles[0][1][1])

	for pat in patentes:
		m = randint(0,len(carFiles)-1)
		marca = str(carFiles[m][0])
		n = randint(1,len(carFiles[m])-1)
		modelo = str(carFiles[m][n][0])

		año = str(randint(int(carFiles[m][n][1]),int(carFiles[m][n][2])))

		color = str(colores[randint(0,len(colores)-1)])

		#print(marca,modelo,año,pat,color)
		#autos.append({"marca":marca,"modelo":modelo,"año":año,"patente":pat,"color":color})
		line = marca + ";" + modelo + ";" + año + ";" + pat + ";" + color
		autos.append(line)

	generador_archivo(autos,f[0])