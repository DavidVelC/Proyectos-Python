#p126-procesar-diccionario.py

print('\033c', end='')

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres, sueldos))

print('Diccionario de nomina:')
print(nomina)

print('\nMostrando solo las llaves:')
for llave in nomina.keys():
    print(llave)

print('\nMostrando solo los valores:')
for valor in nomina.values():
    print(valor)

print('\nIterando por las llaves y accediendo al valor:')
for llave in nomina:
    print(f'{llave}: {nomina[llave]}')

print('\nMostrando llaves y valores con items():')
for llave, valor in nomina.items():
    print(f'{llave}: ${valor:.2f}')

print('\nCalculo de la suma total de los sueldos:')
total = sum(nomina.values())
print(f'Total de sueldos: ${total:.2f}')

print('\nCalculo del promedio de los sueldos:')
promedio = total / len(nomina)
print(f'Promedio de sueldos: ${promedio:.2f}')

print('\nProceso finalizado')
