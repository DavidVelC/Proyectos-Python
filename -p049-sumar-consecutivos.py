#-p049-sumar-consecutivos.py
# Sumar numeros consecutivos hasta una cantidad dada

print('\033[2J\033[H', end='')
print('Suma de numeros consecutivos')

n = int(input('Hasta que numero quieres sumar ? '))

suma = 0
c = 1

while c <= n:
    suma += c
    c += 1

print(f'\nLa suma de los numeros del 1 al {n} es: {suma}')

print('\nProceso terminado')