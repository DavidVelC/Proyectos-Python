#p075-triangulo-caracter.py
print('\033[2J\033[H', end='')
print('Tablas de multiplicar')

r = int(input('Tamaño: '))
c = input('Caracter deseado: ')
for i in range (1, r+1):
    for j in range (1, i+1):
        print(f'{c}', end='')
    print()