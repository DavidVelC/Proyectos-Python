#-p066-conteo-ascendente-for-v2.py
print('\033[H\033[J')
print('Imprime numeros del 1 al 100 en m intervalos de n')
n=int(input('Hasta que numero: '))
m=int(input('Intervalo: '))
for i in range(1, n+1, m):
    print(i)
print('FINISH')
