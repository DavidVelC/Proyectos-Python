#p082-cuadro-hueco-caracter.py
print('\033[2J\033[H', end='')
print('Cuadro hueco')

l = int(input('Tamaño de la lado del cuadrado: '))
c = input('Ingresa el caracter para construir la figura: ')
for i in range (1, l+1):
    for j in range (1, l+1):
        if i == 1 or i == l or j == 1 or j == l:
            print(f'{c}', end='')
        else:
            print(' ', end='')
    print()