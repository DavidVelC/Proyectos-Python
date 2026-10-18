#p124-agregar-diccionario.py

print('\033c', end='')

ventas = {
    'Juan': 1550,
    'Jose': 2600,
    'Maria': 2220
}

print('Diccionario inicial:')
print(ventas)

print('\nAgregando vendedores:')

ventas['Rocio'] = 2500
ventas['Mateo'] = 1567

ventas.update({'Andrea': 9567})
ventas.update({'Miguel': 1234})

print('\nDiccionario actualizado:')
print(ventas)

print('\nfinhshg')
