#p087-modificar-lista.py
# Modificar los elementos de una lista

# Borrar pantalla
print('\033[H\033[J')  # Limpiar pantalla
print('Modificar los elementos de una lista')

califs = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print('\nLongitud y contenido de las calificaciones:')
print(f'Longitud: {len(califs)}')
print(f'Contenido: {califs}')

print('\nModificación de elementos: 0 y 1')
califs[0] = 10.5
califs[1] = 9.5
print(f'Contenido actualizado: {califs}')
print('FInish')