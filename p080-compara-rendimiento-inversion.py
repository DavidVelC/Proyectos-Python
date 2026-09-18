#p080-compara-rendimiento-inversion.py

print('\033[2J\033[H', end='')
print('Comparacion de fondos de inversion')
print('-'*30)
print('\n--- Fondo 1 ---')
fondo1 = float(input('Monto inicial: '))
tasa1 = float(input('Tasa de interes anual (%): '))

print('\n--- Fondo 2 ---')
fondo2 = float(input('Monto inicial: '))
tasa2 = float(input('Tasa de interes anual (%): '))

years = int(input('\nNumero de años a proyectar: '))

saldo1 = fondo1
saldo2 = fondo2

print('\nAño\tFondo 1\t\tFondo 2')
print('----------------------------------------')

for years in range(1, years + 1):
    saldo1 = saldo1 + (saldo1 * tasa1 / 100)
    saldo2 = saldo2 + (saldo2 * tasa2 / 100)

    print(f'{years}\t${saldo1:.2f}\t\t${saldo2:.2f}')

rendimiento1 = saldo1 - fondo1
rendimiento2 = saldo2 - fondo2

print('\n', '-'*30)
print(f'Rendimiento del Fondo 1: ${rendimiento1:.2f}')
print(f'Rendimiento del Fondo 2: ${rendimiento2:.2f}')

if rendimiento1 > rendimiento2:
    print('\nEl Fondo 1 genero un mayor rendimiento.')
elif rendimiento2 > rendimiento1:
    print('\nEl Fondo 2 genero un mayor rendimiento.')
else:
    print('\nAmbos fondos generaron el mismo rendimiento.')

print('\nFINish')