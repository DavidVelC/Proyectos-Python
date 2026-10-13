#p118-lote-autos.py
#Crear una lista de diccionarios para representar un lote de autos
autos = [
{ 'marca':'Ford', 'Modelo':'Mustang', 'año': 1964 },
{ 'marca':'VW', 'Modelo':'Jetta', 'año': 2015 },
{ 'marca':'Toyota', 'Modelo':'Camry', 'Año':2020}
]
autos.append({ 'marca':'Chevrolet', 'modelo':'Malibu', 'año': 2022 })
print('\033[H\033[J')
print('='*50)
print('Listado de Autos')
print('='*50)
print(f'\nTodos los autos : {autos} \nTotal: {len(autos)}')
print('\nCada auto dentro de los autos:')
print('-'*50)
for auto in autos:
    print(auto)

print('\nDatos en forma de Tabla:')
print('-'*50)
for k in autos[0].keys():
    print(f'{k:<10}\t', end=' | ')
print('\r')
for auto in autos:
    for v in auto.values():
        print(f'{v:<10}\t', end=' | ')
    print('\r')
print('\nDatos en forma de Registro')
print('-'*50)
for auto in autos:
    for k,v in auto.items():
        print(f'{k:<10} : {v:>10}')
print('')
print('finish')