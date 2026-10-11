#p110-comprension-filtra-palabras.py
# Filtrar palabras de mas de 4 caracteres y convertirlas a mayusculas

print('\033[H\033[J')
print('Filtrar palabras\n')

texto = input('Introduce palabras separadas por espacios: ')

palabras = texto.split()

filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 4]

print(f'\nLista original: {palabras}')
print(f'Lista filtrada: {filtradas}')

print('\nProceso finalizado')