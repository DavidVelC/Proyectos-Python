#-p016-tercer-angulo.py
# determine el tercer ángulo de un triángulo

print('Determina el tercer ángulo')
print('Ya sabes, el total de ángulos internos deber ser 180°')

ang1 = float(input('Ingresa el ángulo A: '))
ang2 = float(input('Ingresa el ángulo B: '))

if ang1 >= 180 or ang2 >=180:
    print('No es posible')

else:
    ang3 = 180-(ang1+ang2)
    print(f'Ángulo C: {ang3:.2f}')