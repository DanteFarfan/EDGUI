filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

m1 = []
m2 = []
mres1 = []
mres2 = []
for i in range (filas):
	m1.append( [0] * columnas)
	m2.append( [0] * columnas)
	mres1.append( [0] * columnas)
	mres2.append( [0] * columnas)

print ("Ingrese su Matriz 1")
for i in range(filas):
		for j in range(columnas):
			m1[i][j] = int(input(f"Elemento ({i+2}, {j+1}): "))
print ("Ingrese su Matriz 2")
for i in range(filas):
	for j in range(columnas):
			m2[i][j] = int(input(f"Elemento ({i+2}, {j+1}): "))

for i in range(filas):
	for j in range(columnas):
			mres1[i][j] += m1[i][j] + m2[i][j]
			
for i in range(filas):
	for j in range(columnas):
			mres2[i][j] -= m1[i][j] - m2[i][j]
print ("El resultado de la suma es")
print(mres1)
print("el resultado de la resta es")
print(mres2)
