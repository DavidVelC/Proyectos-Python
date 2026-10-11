#p107-listas-aleatorios-suma.py
# Sumar elementos correspondientes si ambos son impares

from random import randint
print('\033[H\033[J')
print('Suma de numeros impares de dos listas\n')

lista_a = []
lista_b = []
lista_c = []

for i in range(10):
    lista_a.append(randint(1, 100))
    lista_b.append(randint(1, 100))

for i in range(10):
    if lista_a[i] % 2 != 0 and lista_b[i] % 2 != 0:
        lista_c.append(lista_a[i] + lista_b[i])
    else:
        lista_c.append(0)

print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')
print(f'Lista C: {lista_c}')