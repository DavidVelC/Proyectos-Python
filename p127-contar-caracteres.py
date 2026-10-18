#p127-contar-caracteres.py

print('\033c', end='')

print('Frecuencia de caracteres\n')

texto = input('Introduce una cadena de texto: ')

frecuencia = {}

for caracter in texto:
    if caracter not in frecuencia:
        frecuencia[caracter] = 1
    else:
        frecuencia[caracter] += 1

print('\nDiccionario de frecuencia:')
print(frecuencia)

print('\nProceso finalizado')
