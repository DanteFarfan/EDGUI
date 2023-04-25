import random

filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

m1 = []
m2 = []
m3 = []
mres1 = []
mres2 = []
for i in range (filas):
	m1.append( [0] * columnas)
	m2.append( [0] * columnas)
	m3.append( [0] * columnas)
	mres1.append( [0] * columnas)
	mres2.append( [0] * columnas)

for i in range(filas):
		for j in range(columnas):
			m1[i][j] = random.randrange(0, 5)

for i in range(filas):
	for j in range(columnas):
			m2[i][j] = random.randrange(0, 5)
			
for i in range(filas):
	for j in range(columnas):
			m2[i][j] = random.randrange(0, 5)

for i in range(filas):
	for j in range(columnas):
			mres1[i][j] += m1[i][j] + m2[i][j]
			
for i in range(filas):
	for j in range(columnas):
			mres2[i][j] -= m2[i][j] - mres1[i][j]

print ("El resultado de la suma es")
print(mres1)
print("el resultado de la resta es")
print(mres2)