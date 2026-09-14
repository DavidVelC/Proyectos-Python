#-p069-arriba-abajo.py
print('\033[H\033[J')
print('imprime numoers de 1 a n o n a 1 segun tu selección')
print('[ 1 ] Voy de 1 a n')
print('[ 2 ] Voy de n a 1')
op = int(input('Elige ? '))

if op == 1:
    print('\nVamos hacia arriba de 1 a n')
    n = int(input('Hasta donde ? '))
    for x in range(1, n+1, 1):
        print(f'{x} ', end='')

elif op == 2:
    print('\nVamos hacia abajo de n a 1')
    n = int(input('Desde donde ? '))
    for x in range(n, 0, -1):
        print(f'{x} ', end='')

else:
    print('\n\nOpcion Erronea')

print('\n\nProceso Terminado')