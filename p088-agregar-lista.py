#p088-agregar-lista.py
# Agregar elementos a una lista

# Borrar pantalla
print('\033[H\033[J')  # Limpiar pantalla
print('Agregar elementos a una lista')

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print('\nLongitud y contenido la lista de numeros:')
print(f'Contenido: {nums} | Longitud: {len(nums)}')

print('\n Agregar 90 y 100 al final de la lista')
nums.append(90)
nums.append(100)
print(f'Contenido actualizado: {nums} | Longitud: {len(nums)}')

print('\n Insertar 80 en la posición 4')
nums.insert(4, 80)
print(f'Contenido actualizado: {nums} | Longitud: {len(nums)}')

print('\nExtender la lista con otra lista [110, 120, 130]')
nums.extend([110, 120, 130])
print(f'Contenido actualizado: {nums} | Longitud: {len(nums)}')
print('finish')