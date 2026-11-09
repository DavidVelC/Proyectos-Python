#p144-tabla-multiplicar.py
def tabla_multiplicar(tabla: int, limite: int) -> None:
    print(f'Tabla de multiplicar del {tabla} hasta el {limite}:')
    for i in range(1, limite + 1):
        resultado = tabla * i
        print(f'{tabla} x {i} = {resultado}')

tabla = int(input('Ingrese la tabla de multiplicar: '))
limite = int(input('Limite de la tabla: '))
tabla_multiplicar(tabla, limite)