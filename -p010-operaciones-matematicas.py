#-p010-operaciones-matematicas.py 
# usar operadoers matematicos
print('\033[2J\033\[H', end='')

print("="*50)
print(" CALCULADORA DE OPERACIONES MATEMÁTICAS")
print("="*50)

# Solicitar números al usuario

x = float(input('Ingresa el primer número (x): '))
y = float(input('Ingresa el segundo número (y): '))
print(f"\nRESULTADOS CON x = {x} y y = {y}")
print("-" * 40)

suma = x+y
resta = x-y
mult = x*y
div = x/y
mod = x%y
pot = x**y
dive = x//y

print(f'Suma: {suma:>20.3f}')
print(f'Resta: {resta:>20.3f}')
print(f'Multiplicación: {mult:>20.3f}')
print(f'División: {div:>20.3f}')
print(f'Módulo: {mod:>20.3f}')
print(f'Potenciación: {pot:>20.3f}')
print(f'División entera: {dive:>20.3f}')
print(f'Suma: {suma:>20.3f}')
print("-" * 40)

#alinear formato :>10
