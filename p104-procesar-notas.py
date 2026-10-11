#p104-procesar-notas.py
#p118-procesar-notas.py
# Procesar notas y calcular estadisticas

print('\033[H\033[J')
print('Procesador de notas\n')
print('Introduce notas entre 0 y 100 (0 para terminar)\n')

notas = []
suma = 0

while True:
    try:
        n = float(input('Nota > '))

        if n == 0:
            break

        if 0 < n <= 100:
            notas.append(n)
            suma += n
        else:
            print('Error: la nota debe estar entre 0 y 100.')

    except ValueError:
        print('Error: debes ingresar un numero.')

if notas:
    promedio = suma / len(notas)
    maxima = max(notas)
    minima = min(notas)

    menores = []

    for nota in notas:
        if nota < promedio:
            menores.append(nota)

    print('\nResultados')
    print(f'Cantidad de notas: {len(notas)}')
    print(f'Lista de notas: {notas}')
    print(f'Suma de las notas: {suma:.2f}')
    print(f'Promedio: {promedio:.2f}')
    print(f'Nota maxima: {maxima}')
    print(f'Nota minima: {minima}')
    print(f'Cantidad de notas menores al promedio: {len(menores)}')
    print(f'Notas menores al promedio: {menores}')

else:
    print('No se introdujeron notas.')

print('\nProceso finalizado')