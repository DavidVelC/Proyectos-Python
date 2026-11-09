#p145-cuadro-caracter.py
def dibuja_cuadro(ancho: int, alto: int, caracter: str) -> None:
    for r in range(ancho):
        for c in range(alto):
            print(caracter, end='')
        print('') 

# Solicita al usuario los datos
renglones = int(input('Ingrese el número de renglones del cuadro: '))
columnas = int(input('Ingrese el número de columnas del cuadro: '))
caracter = input('Ingrese el carácter para dibujar el cuadro: ')
dibuja_cuadro(renglones, columnas, caracter)