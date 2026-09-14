# p033-aceptar-estudiante-v2.py
# Aceptar a un estudiante en base a la edad y calificaciones v2
name = input('Nombre: ')
edad = int(input('Edad: '))
if edad >= 18:
    print(f'\n{nombre}, ingresa ambas calificaciones')
    c1 = float(input('Ingresa tu primer calificación: '))
    c2 = float(input('Ingresa tu segunda calificación: '))
    
    if c1 >= 8 and c2 >= 8:
        print(f' ¡Bienvenid@, {name}! Tu edad de {edad} y tus calificaciones te permiten ingresar.')
    else:
        print('\nAspirante rechazado por bajas calificaciones')

else:
    print(f'No se aceptan menores de 18')
print('FInish')