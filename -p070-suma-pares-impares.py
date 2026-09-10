#-p070-suma-pares-impares.py

print('\033[21\033[H', end='')
print('Imprime numeros pares o impares de 1 a n segun lo decidas')
print('[ 1 ] Voy de 1 a n con pares')
print('[ 2 ] Voy de 1 a n con impares')
op = int(input('Selección: '))
suma = 0

if op==1:
    print('\nDe 1 a n con pares')
    n = int(input('Rango '))
    for x in range(2, n+1, 2):
        print(f'{x} ', end='')
        suma = suma + x
    print('\nSuma = ' + str(x))

elif op==2:
    print('\nDe 1 a n con impares')
    n = int(input('Rango: '))
    for x in range(1, n+1, 2):
        print(f'{x} ', end='')
        suma = suma + x
    print('Suma = ' + str(x))

else:
    print('\n\nOpcion Erronea')

print('\n\nFinish')