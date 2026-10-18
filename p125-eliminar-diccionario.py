#p125-eliminar-diccionario.py

print('\033c', end='')

municipios = {
    'Apozol': 1863,
    'Calera': 1868,
    'Fresnillo': 1554,
    'Guadalupe': 1821,
    'Jalpa': 1824,
    'Jerez': 1824,
    'Loreto': 1931,
    'Mazapil': 1824,
    'Momax': 1857
}

print('Diccionario inicial:')
print(municipios)

print('\nEliminando Apozol con del:')
del municipios['Apozol']
print(municipios)

print('\nEliminando Fresnillo con pop():')
municipios.pop('Fresnillo')
print(municipios)

print('\nEliminando el ultimo elemento con popitem():')
municipios.popitem()
print(municipios)

print('\nVaciando el diccionario con clear():')
municipios.clear()
print(municipios)

print('\nfinsh')
