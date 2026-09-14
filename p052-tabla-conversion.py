# p052-tabla-conversion.py

tc = 16.80

while True:

    print('\033[2J\033[H', end='')
    print('Imprime una tabla de conversion de peso a dolar')
    print(f'Tipo de cambio: {tc}')
    print('-' * 40)

    while True:

        inicial = float(input('Valor inicial del rango: '))
        final = float(input('Valor final del rango: '))

        if (inicial > 0 and final > 0) and inicial < final:
            break
        else:
            print('Inicial debe ser menor al final')

    c = inicial

    print('\nPesos\tDollar')
    print('-' * 15)

    while c <= final:
        print(f'{c}\t{c/tc:.2f}')
        c += 1

    print('-' * 15)

    res = input('Deseas Continuar (S/N)? ').upper()

    if res == 'N':
        break

print('\nProceso terminado')