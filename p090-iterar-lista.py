#p090-iterar-lista.py
# Recorrer elementos de una lista
print('\033[H\033[J')  # Limpiar pantalla
print('Procesando una lista de numeros')

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print('\nLongitud y contenido de la lista de numeros:')
print(f'Contenido: {nums} | Longitud: {len(nums)}')


print('\nImprimir cada numero de la lista')
for num in nums:
    print(f'Numero: {num}')


print('\nImprimir los numeros accediendo por su indice')
for i in range(len(nums)):
    print(f'Indice: {i} | Numero: {nums[i]}')


print('\nNueva secuencia sumando 2 a cada numero')
nums_mas_2 = []

for num in nums:
    nums_mas_2.append(num + 2)

print(f'Lista original: {nums}')
print(f'Nueva secuencia: {nums_mas_2}')


print('\nNueva secuencia sumando 10 a cada numero usando su indice')
nums_mas_10 = []

for i in range(len(nums)):
    nums_mas_10.append(nums[i] + 10)

print(f'Lista original: {nums}')
print(f'Nueva secuencia: {nums_mas_10}')

print('Finish')