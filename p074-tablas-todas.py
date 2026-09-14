#p074-tablas-todas.py
print('\033[2J\033[H', end='')
print('Tablas de multiplicar')

t = 10
n = 10
for i in range (1, t+1):
    print("="*30)
    print(f'tabla del {i}')
    print("="*30)
    for j in range (1, n+1):
        print(f'{i} X {j} = {i*j}')
    print('='*30)
print('finish')
