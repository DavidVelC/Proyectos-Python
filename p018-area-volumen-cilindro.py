#-p018-area-volumen-cilindro.py
#calcule el área y volumen de un cilindro.
import math as mt

print('calcule el área y volumen de un cilindro')
rad = float(input('Ingresa el radio del cilindro: '))
h = float(input('Ingresa la altura del cilindro: '))

area = 2*mt.pi*(rad+h)
volume = mt.pi*(rad**2)*h

print(f'El área del cilindro es: {area:.2f} m**2')
print(f'El volumen del cilindro es: {volume:.2f} m**3')
