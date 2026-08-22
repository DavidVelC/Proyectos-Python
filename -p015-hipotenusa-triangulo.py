#-p015-hipotenusa-triangulo.py
# Crea un programa que calcule la longitud de la hipotenusa de un triángulo rectángulo. 
# El programa debe solicitar
# al usuario que ingrese la longitud de los dos lados (catetos) del triángulo.

import math as mt

print('Calcula la hipotenusa')
catA = float(input(' Introduce el cateto A: '))
catB = float(input(' Introduce el cateto B: '))

hip = mt.sqrt((catA**2)+(catB**2))

print(f'Hipotenus: {hip}')