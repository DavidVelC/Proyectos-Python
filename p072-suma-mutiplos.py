#p072-suma-mutiplos.py
# Imprime numeros de 1 a n, solo los multiplos de m

print('\033[2J\033[H', end='')
print('Imprime numeros de 1 a n, solo los multiplos de m')

m = int(input('Múltiplos '))
n = int(input('Límites: '))

c = s = 0

for i in range(1, n+1):
    if i % m == 0:
        print(f'{i} ', end=' ')
        c += 1
        s += i

print(f'\n\nCuantos multiplos fueron {c}')
print(f'Suma de los multiplos de {m} = {s}')