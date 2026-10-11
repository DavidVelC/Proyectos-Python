#p105-listas-multiplica.py
print('\033[H\033[J')
print('Multiplica dos listas\n')
print('Introduce notas entre 0 y 100 (0 para terminar)\n')

listA = []
listB = []
listC = []

print('Introduzca 5 numeros para la Lista A:')

for i in range(5):
    n = int(input(f'A[{i}]: '))
    listA.append(n)

print('\nIntroduzca 5 numeros para la Lista B:')

for i in range(5):
    n = int(input(f'B[{i}]: '))
    listB.append(n)

for i in range(5):
    producto = listA[i] * listA[i]
    listC.append(producto)

print('\n--- Resultados ---')
print(f'Lista A: {listA}')
print(f'Lista B: {listB}')
print(f'Lista C (A * B): {listC}')