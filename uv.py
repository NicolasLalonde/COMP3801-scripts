import copy
import math

def mult(A, B):
	result = [[0 for j in range(len(B[0]))]for i in range(len(A))]
	for i in range(len(A)):
		for j in range(len(B[0])):
			for k in range(len(B)):
				result[i][j] += A[i][k] * B[k][j]
	return result

def transpose(A):
	result = [[0 for j in range(len(A))]for i in range(len(A[0]))]
	for i in range(len(A)):
		for j in range(len(A[0])):
			result[j][i] = A[i][j]
	return result

def printMatrix(matrix):
	print("\\begin{bmatrix}")
	for row in range(len(matrix)):
		for column in range(len(matrix[row])):
			print(str(matrix[row][column]), end='')
			if column!=len(matrix[row])-1:
				print(" & ", end='')
			else:
				print("\\\\")
	print("\\end{bmatrix}")

def rmse(A, B):
	result=0
	for row in range(len(A)):
		for column in range(len(A[row])):
			if not ignore[row][column]:
				result+=(A[row][column] - B[row][column])**2
	elems = len(A) * len(A[0])
	result = math.sqrt(result/elems)
	return result

def input_int(prompt):
	while True:
		try:
			res=int(input(prompt))
			return res
		except:
			print("Please input integer!")
			continue


M=[
[4, 0],
[5, 1],
[0, 1]
]

ignore=[
[False, True],
[False, False],
[True, False]
]

U=[
[1],
[1],
[1]
]

V=[
[1, 1]
]


def modifU(r, s):
	result = copy.deepcopy(U)
	numerator=0
	denominator=0
	for j in range(len(M[0])):
		if ignore[r][j]:
			continue
		sumk=0
		for k in range(len(V)):
			if k != s:
				sumk += U[r][k] * V[k][j]
		numerator += V[s][j] * (M[r][j] - sumk)
		denominator += V[s][j]**2
	result[r][s] = numerator/denominator
	return result


def modifV(r, s):
	result = copy.deepcopy(V)
	numerator=0
	denominator=0
	for i in range(len(M)):
		if ignore[i][s]:
			continue
		sumk=0
		for k in range(len(V)):
			if k != r:
				sumk += U[i][k] * V[k][s]
		numerator += U[i][r] * (M[i][s] - sumk)
		denominator += U[i][r]**2
	result[r][s] = numerator/denominator
	return result

def printCurrent(U, V):
	print("================")
	print("$$", end='')
	printMatrix(U)
	print("\\times")
	printMatrix(V)
	print("=")
	prod=mult(U,V)
	printMatrix(prod)
	print("$$")
	print("RMSE: ", end='')
	print(rmse(M, prod))
	print("================")

def iteration():
	global U
	global V
	for row in range(len(U)):
		for col in range(len(U[0])):
			U=modifU(row, col)
	for row in range(len(V)):
		for col in range(len(V[0])):
			V=modifV(row, col)


while True:
	matrix = input('U or V: ')
	if matrix == "M":
		printMatrix(M)
		continue
	elif matrix == "R":
		printCurrent(U, V)
		continue
	elif matrix == "U":
		mod=U
	elif matrix == "V":
		mod=V
	elif matrix== "I":
		times = input_int("How many times? ")
		for i in range(times):
			iteration()
		printCurrent(U, V)
		continue
	else:
		print("Invalid input!")
		continue
	row = input_int('row: ')
	if row > len(mod):
		print("row too big!")
		continue
	row -= 1
	col = input_int('column: ')
	if col > len(mod[0]):
		print("column too big!")
		continue
	col-= 1
	if matrix == "U":
		modU=modifU(row, col)
		printCurrent(modU, V)
		keep=input("Keep?[y/n]: ")
		if keep == "y":
			U=modU
	elif matrix == "V":
		modV=modifV(row, col)
		printCurrent(U, modV)
		keep=input("Keep?[y/n]: ")
		if keep == "y":
			V=modV
