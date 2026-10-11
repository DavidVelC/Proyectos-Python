#p111-comprension-pares-cuadrados.py
# Cuadrados de numeros pares usando comprension de listas

print('\033[H\033[J')
print('Cuadrados de numeros pares\n')

n = int(input('Introduce el valor de n: '))

numeros = [i for i in range(1, n + 1)]

cuadrados = [num ** 2 for num in numeros if num % 2 == 0]

suma = sum(cuadrados)

print(f'\nLista completa: {numeros}')
print(f'Cuadrados de numeros pares: {cuadrados}')
print(f'Suma de los cuadrados: {suma}')

print('\nProceso finalizado')