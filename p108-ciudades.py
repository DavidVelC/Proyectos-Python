#p108-ciudades.py
# Leer ciudades y clasificarlas segun su letra inicial

print('\033[H\033[J')
print('Lista de ciudades\n')
print("Introduce nombres de ciudades ('$' para terminar)\n")

ciudades = []
consonantes = []
vocales = 'AÁEÉIÍOÓUÚ'

while True:
    ciudad = input('Ciudad > ').strip()

    if ciudad == '$':
        break

    if ciudad != '':
        ciudades.append(ciudad)

for ciudad in ciudades:
    inicial = ciudad[0].upper()

    if inicial.isalpha() and inicial not in vocales:
        consonantes.append(ciudad)

print('\n--- Resultados ---')
print(f'Cantidad de ciudades: {len(ciudades)}')
print(f'Lista completa: {ciudades}')

ciudades.sort(reverse=True)
print(f'Lista en orden descendente: {ciudades}')

print(f'Cantidad de ciudades que inician con consonante: {len(consonantes)}')
print(f'Ciudades que inician con consonante: {consonantes}')

print('\nProceso finalizado')