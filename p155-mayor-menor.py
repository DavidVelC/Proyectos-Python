#p155-mayor-menor.py
def captura_datos() -> list[float]:
    datos = []
    print("Ingresa números (escribe 'fin' para terminar):")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            datos.append(numero)
        except ValueError:
            print("Por favor, ingresa un número válido o 'fin'para terminar.")

    return datos

def mayor(lista: list[float]) -> float:
    mayor_num = lista[0]
    for numero in lista:
        if numero > mayor_num:
            mayor_num = numero
    return mayor_num

def menor(lista: list[float]) -> float:
    menor_num = lista[0]
    for numero in lista:
        if numero < menor_num:
            menor_num = numero
    return menor_num

#principal
num = captura_datos()
print(f'Los numeros capturados son: {num}')
mayor = mayor(num)
print(f'El numero mayor es: {mayor}')
menor = menor(num)
print(f'El numero mayor es: {menor}')