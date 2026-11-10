#p153-suma-lista.py
#suma elementos de una lista
def sumaList(lista: list[float]) -> float:
    suma = 0.0
    for num in lista:
        suma += num
    return suma

# progframa principal
numeros = [1.5, 2.3, 3.7, 4.1]
resultado = sumaList(numeros)
print(f"La suma de la lista es: {resultado}")