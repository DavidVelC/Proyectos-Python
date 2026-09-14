#-p021-distancia-entre-puntos.py
#calcule la distancia entre dos puntos en un plano cartesiano.
import math

print('Calcula la distancia entre dos puntos en un plano cartesiano x, y')

x1 = float(input("Ingresa la coordenada x1 para el Punto A: "))
y1 = float(input("Ingresa la coordenada y1 para el Punto A: "))
print('-'*50)
x2 = float(input("Ingresa la coordenada x2 para el Punto B: "))
y2 = float(input("Ingresa la coordenada y2 para el Punto B: "))

dist = math.sqrt(((x2-x1)** 2) + ((y2-y1)**2))

print(f'La distancia es: {dist:.2f}')
