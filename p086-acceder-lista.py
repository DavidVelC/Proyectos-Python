#p086-acceder-lista.py
print('\033[2J\033[H', end='')
print('Acceder a los elementos de una lista')

print('\nLongitud y contenido de las mediciones:')
print(f'Longitud: {len(nums)}')
print(f'Contenido: {nums}')

print('\nPor indice positivo:')
print(f'Elemento en el indice 0 y 8: {nums[0]} - {nums[8]}')

print('\nPor indice negativo:')
print(f'Elemento en el indice -9 y -1: {nums[-9]} - {nums[-1]}')

print('\nPor rango:')
print('\nDe 2 al 6 (sin incluir el 6):')
print(f'Elementos: {nums[2:6]}')

print('\nPor saltos:')
print(f'Elementos con saltos de 2: {nums[::2]}')
print(f'Elementos con saltos de 3: {nums[::3]}')
print('FInish')