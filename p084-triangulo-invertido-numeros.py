#p084-triangulo-invertido-numeros.py
r = int(input('Tamaño: '))
for i in range (r, 0, -1):
    for j in range (i, 0, -1):
        print(f'{j}', end='')
    print()