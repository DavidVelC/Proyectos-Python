#p158-aleatorios.py
import random
def generar_numeros_aleatorios(n: int, min: int, max: int) -> list[int]:
    numeros_aleatorios = []
    for _ in range(n):
        numero = random.randint(min, max)
        numeros_aleatorios.append(numero)
    return numeros_aleatorios
def sumar_listas(lista1: list[int], lista2: list[int]) -> list[int]:
    suma = []
    for a, b in zip(lista1, lista2):
        suma.append(a + b)
    return suma

#principal
MAX = 10
lista1 = generar_numeros_aleatorios(MAX, 1, 10)
lista2 = generar_numeros_aleatorios(MAX, 50, 100)
lista3 = sumar_listas(lista1, lista2)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
if lista3 == 0:
    print('No tienen la misma longitud, no se pueden sumar')
else:
    print(f"Suma de listas: {lista3}")