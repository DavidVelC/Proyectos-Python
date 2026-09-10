#-p068-conteo-descendente-for-v2.py
print('\033[H\033[J')
print('Imprime numeros en decreciente en m intervalos de n')
n=int(input('Desde que numero: '))
m=int(input('Intervalo: '))
for i in range(n, 0, -m):
    print(i)
print('FINISH')