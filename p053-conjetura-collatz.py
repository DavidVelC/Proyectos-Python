# p053-conjetura-collatz.py
# Dado n, si es par n/2, si es impar 3*n+1 hasta llegar a 1
print('Imprime la secuencia de Collatz')
while True:

    print('\033[2J\033[H', end='')
    print('Imprime la secuencia de Collatz')

    n = int(input('Ingresa n (positivo entero): '))

    while n != 1:

        print(f'{n} ', end=' ')

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1

    print(n)

    if input('\nDeseas continuar? (S/N) ').upper() == 'N':
        break

print('Finish')