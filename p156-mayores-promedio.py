#p156-mayores-promedio.py
#calcula el promedio
def promedio_lista(lista: list[float]) -> float:
    suma = 0.0
    if not lista:
        return 0.0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def mayores_al_promedio(lista: list[float], prom: float) -> list[float]:
    mayores = []
    for numero in lista:
        if numero > prom:
            mayores.append(numero)
    return mayores

numeros = [12.22, 1.5, 2.3, 3.7, 4.1, 10.22, 34.5]
print(f'Los numeros son: {numeros}')
prom = promedio_lista(numeros)
print(f'EL promedio es {prom:.2f}')
resultado = mayores_al_promedio(numeros, prom)
print(f"Números mayores al promedio: {resultado}")