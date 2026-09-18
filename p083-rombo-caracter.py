#p083-rombo-caracter.py
print('\033[2J\033[H', end='')

print('Rombo')

n = int(input('Tamaño del rombo (numero impar): '))
c = input('Ingresa el caracter para construir la figura: ')

mitad = n // 2

for i in range(1, mitad + 2):
    espacios = mitad - i + 1
    caracteres = 2 * i - 1

    print(' ' * espacios + c * caracteres)

for i in range(mitad, 0, -1):
    espacios = mitad - i + 1
    caracteres = 2 * i - 1

    print(' ' * espacios + c * caracteres)