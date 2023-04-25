import random

filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
escalar = int(input("Ingrese un numero "))

m1 = []
mres1 = []

for i in range (filas):
	m1.append( [0] * columnas)
	mres1.append( [0] * columnas)
	

for i in range(filas):
		for j in range(columnas):
			m1[i][j] = random.randrange(0, 10)
			
for i in range(filas):
	for j in range(columnas):
			mres1[i][j] = m1[i][j] * escalar
			
print ("El resultado de la multiplicacion es")
print(mres1)

