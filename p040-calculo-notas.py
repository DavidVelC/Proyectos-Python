#-p040-calculo-notas.py
# Calcular el promedio de 5 calificaciones y mostrar el resultado

print('\033[2J\033[H', end='')
print('Calcular promedio de 5 calificaciones')

c1 = float(input('Calificacion 1: '))
c2 = float(input('Calificacion 2: '))
c3 = float(input('Calificacion 3: '))
c4 = float(input('Calificacion 4: '))
c5 = float(input('Calificacion 5: '))

promedio = (c1 + c2 + c3 + c4 + c5) / 5

print(f'\nTu promedio es: {promedio:.2f}')

if promedio < 6:
    print('Quedas reprobado')
elif promedio < 7:
    print('Pasas de panzazo')
elif promedio < 8:
    print('Muy bien, puedes mejorar')
elif promedio < 9:
    print('Excelente, sigue así')
elif promedio <= 10:
    print('Perfecto, tu esfuerzo valió la pena')
else:
    print('no previsto')
print('FINISH')