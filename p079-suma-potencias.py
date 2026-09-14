#- p079-suma-potencias.py
print('\033[2J\033[H', end='')
print('Suma de potencias')
x = int(input('Ingresa el numero: '))
n = int(input('Ingresa la potencia:'))
s=0
print(f'Calculando la serie de s = x^1 + ... + x^{n}\n')
for i in range (1, n+1):
    t=1
    for j in range (i):
        t = t*x
    print(f"{x}^{i} {'+' if i<n else ''}", end='')
    s = s+t
print()
    