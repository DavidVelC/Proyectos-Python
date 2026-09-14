# -p014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonométricas básicas
import math as mt
# convertir a radianes
angulo = int(input("Ingresa el ángulo para convertir a rad: "))

rad = mt.radians(angulo)

#funciones basicas
seno = mt.sin(rad)
coseno = mt.cos(rad)
tangente = mt.tan(rad)

grados = mt.degrees(rad)

salida = ('Resumen de funciones\n'
        f'Seno: {seno:.7f}\n'
        f'Cosen: {coseno:.4f}\n'
        f'Tangente: {tangente:.4f}\n'
        f'Angulo {angulo}° = {rad:.4f} rad\n')
print(salida)