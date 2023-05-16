import random

filas1 = int(input("ingrese la cantidad de filas de la primera matriz"))
columnas1 = int(input("ingrese la cantidad de columnas de la primera matriz"))

m1 = []

for i in range (filas1):
	m1.append( [0] * columnas1)
	
for i in range(filas1):
		for j in range(columnas1):
			m1[i][j] = random.randrange(0, 5)

print("La primera matriz es: ", m1)

filas2 = int(input("ingrese la cantidad de filas de la segunda matriz"))
columnas2 = int(input("ingrese la cantidad de columnas de la segunda matriz"))

m2 = []

for i in range (filas2):
	m2.append( [0] * columnas2)
	
for i in range(filas2):
		for j in range(columnas2):
			m2[i][j] = random.randrange(0, 5)

print("La segunda matriz es: ", m2)

if filas1 == filas2 and columnas1 == columnas2:
    mres = []

    for i in range (filas2):
        mres.append( [0] * columnas2)
        
    for i in range(filas2):
            for j in range(columnas2):
                mres[i][j] = m1[i][j] + m2[i][j]
    print(mres)

    mres2 = []

    for i in range (filas2):
        mres.append( [0] * columnas2)
        
    for i in range(filas2):
            for j in range(columnas2):
                mres2[i][j]*random.randrange(0, 10)

    print(mres2)
		
else:
    print("la cantidad de filas y columnas debe ser igual para ambas matrizes")