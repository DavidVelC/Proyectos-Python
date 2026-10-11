#p109-lista-impares.py
# Primeros n numeros impares y sus operaciones

print('\033[H\033[J')
print('Procesamiento de numeros impares\n')

n = int(input('Cuantos numeros impares deseas generar?: '))

numeros = []
divisibles = []
suma = 0
suma_divisibles = 0

for i in range(n):
    numero = 2 * i + 1
    numeros.append(numero)
    suma += numero

promedio = suma / n

for numero in numeros:
    if numero % 3 == 0:
        divisibles.append(numero)
        suma_divisibles += numero

print('\n--- Resultados ---')
print(f'Lista de numeros impares: {numeros}')
print(f'Suma: {suma}')
print(f'Promedio: {promedio:.2f}')
print(f'Numeros divisibles entre 3: {divisibles}')
print(f'Suma de los divisibles entre 3: {suma_divisibles}')

buscar = int(input('\nQue numero deseas buscar?: '))

if buscar in numeros:
    print(f'El numero {buscar} si esta en la lista.')
    print(f'Indice: {numeros.index(buscar)}')
else:
    print(f'El numero {buscar} no esta en la lista.')

print('\nProceso finalizado')