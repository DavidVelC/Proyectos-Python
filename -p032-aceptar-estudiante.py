# p032-aceptar-estudiante.py
# Aceptar estudiantes en base a edad y calificaciones ( usando OR )
# Las condiciones edad >= 18 y c1 y c2 >= 8

print('\033[2J\033[H', end='')
print('Aceptar estudiantes en base a edad y calificaciones (usando OR)')

name = input('Nombre: ')
edad = int(input('Edad: '))

if edad < 18:
    print(f'\n{name}, no aceptamos menores de edad.')
else:
    print(f'\n{name}, ingresa ambas calificaciones ..')
    c1 = float(input('Ingresa tu primer calificación: '))
    c2 = float(input('Ingresa tu segunda calificación: '))

    if c1 < 8 or c2 < 8:
        print(f'\n{name}, Aspirante rechazado, calif. insuficiente')
    else:
        print(f'{name} Bienvenido {name} a la Universidad  ')

print('\nFinish')