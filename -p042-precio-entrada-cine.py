# p038-taquilla-cine.py
# Determinar el precio de una entrada según la edad

print('\033[2J\033[H', end='')
print('Taquilla del cine\n')

edad = int(input('Dame tu edad: '))

if edad < 5 and edad>0:
    print('Entrada GRATIS')
elif edad <= 12:
    print('Precio de la entrada: $5')
elif edad <= 64:
    print('Precio de la entrada: $10')
elif edad >= 65:
    print('Precio de la entrada: $7')
else:
    print('no es posible')

print('\nProceso terminado')