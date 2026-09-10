#-p071-suma-promedio-numeros.py
# Calcula la suma y el promedio de n calificaciones

while True:
    print('\033[21\033[H', end='')
    print('Calcula la suma y el promedio de n calificaciones')

    n = int(input('Cantidad de calif. '))
    suma = 0
    strcals = ''

    for i in range(1, n+1, 1):
        cal = int(input(f'Calificacion {i}: '))
        suma += cal
        strcals = strcals + str(cal) + ' '

    print(f'\nLos numeros fueron: {strcals}')
    print(f'Suma : {suma}')
    print(f'Promedio es : {suma/n}')

    if input('\nSeguimos (S/N) ? ').upper() == 'N': break