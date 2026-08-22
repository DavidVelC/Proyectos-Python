#-p022-resistencia-equivalente-paralelo.py
#calcule la resistencia total de un circuito con cuatro 
#resistencias en paralelo

print('Calcule la resistencia total de 4 resistencias en paralelo')
print('Ingresa los valores de 4 resistencias')
r1, r2, r3, r4 = float(input()), float(input()), float(input()), float(input())

req = 1/((1/r1)+(1/r2)+(1/r3)+(1/r4))

print(f'La resistencia total es: {req:.4f}')