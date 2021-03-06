__author__='Enzo Lizama Paredes'

from math import isinf
from helpers import *
from bitwise_manipulation import *
import json, time
from load_matrix import cargar
from read_file import distancia, leerDataSet, imprimirRes
from filter_cpobaldos import readGenerate

a = []
random_size = 10

def choose():
	global a, random_size
	a = readFromFile()

def generateSubsets(n):
	l = []
	for i in range(2**n):
		l.append(i)
	return sorted(l, key = lambda x : size(x) )


def tsp():
	global a
	n = len(a)
	l = generateSubsets(n)
	cost = [ [-1 for city in range(n)] for subset in l]
	p = [ [-1 for city in range(n)] for subset in l]

	pretty(a)
	t1 = time.time()
	count = 1
	total = len(l)
	for subset in l:
		for dest in range(n):
			if not size(subset):
				cost[subset][dest] = a[0][dest]
				#p[subset][dest] = 0
			elif (not inSubset(0, subset)) and (not inSubset(dest, subset)) :
				mini = float("inf")
				for i in range(n):
					if inSubset(i, subset):
						modifiedSubset = remove(i, subset)
						val = a[i][dest] + cost[modifiedSubset][i]
						
						if val < mini:
							mini = val
							p[subset][dest] = i

				if not isinf(mini):
					cost[subset][dest] = mini
		count += 1
	path = findPath(p)
	t2 = time.time()
	diff = t2 - t1
	print(" => ".join(path))

	Cost = cost[2**n-2][0]
	print(Cost)
	imprimirRes(path)
	print("Time Taken: %f milliseconds" % (diff * 1000))


if __name__ =="__main__":
	choice = str(input("Ingresa el nombre del distrito a solucionar:  "))
	readGenerate(choice)
	choose()
	tsp()
