#p102-aplanar-matriz.py
#Aplana una matriz de dos dimensiones a una lista de una dimensión
print('\033[H\033[J')
print("\033[1;34m" + 'Actividad 14 Operaciones con matrices' + "\033[0m")

matrix = [(1, 2, 3), (-4, 5, 6), (-7, 8, 9)]
flat = [elemento for fila in matrix for elemento in fila]
positivos = [elemento for fila in matrix for elemento in fila if elemento>0]
negativos = [elemento for fila in matrix for elemento in fila if elemento<0]


print('Matriz original: ', matrix)
print('Matriz aplanada: ', flat)
print('Numeros positivos: ', positivos)
print('Numero negativos: ', negativos)