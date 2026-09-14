#-p002-area-circulo.py
#Calcula area circulo

import math

print("Cálcula el área del circulo\n")
radio = float(input("radio: "))

area = math.pi * math.pow(radio, 2)

print(f"El area es para un circulo de radio {radio} es: {area:.3f}")