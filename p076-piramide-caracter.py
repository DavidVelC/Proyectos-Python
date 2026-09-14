#- p076-piramide-caracter.py
print('\033[2J\033[H', end='')
print('Tablas de multiplicar')

r = int(input('Tamaño: '))
c = input('Caracter deseado: ')
for i in range (1, r+1):
    espacios = r-i
    car = 2*i-1
    for e in range (espacios):
        print(' ', end='')
    for j in range (car):
        print(c, end='')
    print()