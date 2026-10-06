#p098-cuadrados-lista.py
# Guanaera cuadros usando compresión de listas
print('\033[H\033[J')
print("\033[1;32m" + 'Actividad 14 Cuadrados' + "\033[0m")
print('Cuadrados de 1 a n usando compresión de listas')
n = int(input('Ingrese el valor de n: '))

num = list(range(1, n+1))
square = [i**2 for i in num]

print('Los numeros del 1 al', n, 'son', num)
print('Los cuadrados del 1 al', n, 'son', square)