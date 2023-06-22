import random
from random import randint
file_names = ["file1"]

def load_file_old (file_name:str="test",extension:str=".csv") -> list:
	lista = []
	try:
		file = open(file_name+extension,"r")
	except Exception:
		return None

	for count, line in enumerate(file):
		line = line.strip()
		aux = line.split(";")
		lista.append({"model":aux[0],"year":aux[1].split(",")})
	file.close()
	return lista

def load_file (file_name:str="test",extension:str=".csv") -> list:
	lista = []
	file_name += extension
	file = open(file_name,"r")

	for count, line in enumerate(file):
		line = line.strip()
		aux = line.split(";")
		lista.append(aux)
	file.close()
	return lista


def imprimirLista (lista:list, firstRowIsName:bool=True) -> None:
	for count, row in enumerate(lista):
		if (count == 0):
			if (firstRowIsName):
				print(row)
				continue
		for k in row.keys():
			print(row[k], end = "")
		print()

def generador_patentes (cantidad_patentes:int=100,numeros:int=3,letras:int=3,sep:bool=False,sep_simbol:str="-") -> list:
	lista = []
	random.seed()
	for i in range(cantidad_patentes):
		patente = ""
		
		for n in range(letras):
 			patente += str(chr(randint(65,90)))

		if(sep):
			patente += sep_simbol
		for n in range(numeros):
 			patente += str(randint(1,9))
 		
		lista.append(patente)
	return lista

def generador_archivo (arr:list,file_name:str, extension:str=".csv", clear:bool=True) -> None:
	file_name += extension
	file = open(file_name,"a")
	if (clear):
		clear_file(file_name)

	for i in range(len(arr)-1):
		file.write(str(arr[i])+"\n")
	file.write(arr[-1])
	file.close()

def clear_file (file_name:str) -> None:
	file = open(file_name, "w")
	file.close()

def clear () -> None:
	from os import system
	system("cls")

def pause () -> None:
	from os import system
	system("pause")

lista_patentes = generador_patentes(10,3,3)
generador_archivo(lista_patentes,"test",".csv")

print(load_file("file1"))