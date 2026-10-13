#p119-registro-estudiantes.py
# Crear una lista de diccionarios para representar un registro de estudiantes

grupo = [
    {'Nombre':'Carlos Garcia','Edad':23,'Carrera':'Sistemas','Promedio':8.5},
    {'Nombre':'Maria Lopez','Edad':22,'Carrera':'Medicina','Promedio':9.2},
    {'Nombre':'Juan Pérez','Edad':24,'Carrera':'Sistemas','Promedio':8.2}
]

print('\033c', end='')
print('Registro de Estudiantes\n')
print(f"\nGrupo de estudiantes:\n{'-'*60}\n{grupo} - {len(grupo)}")

print('\nCaptura de nuevos estudiantes')

while True:
    print('Datos Estudiante:')
    nombre = input('Nombre: ')

    if nombre != '':
        edad = int(input('Edad: '))
        carrera = input('Carrera: ')
        promedio = float(input('Promedio: '))

        grupo.append({
            'Nombre': nombre,
            'Edad': edad,
            'Carrera': carrera,
            'Promedio': promedio
        })
    else:
        print('No se ingresaron más datos')
        break

print(f"\nGrupo de estudiantes completo:\n{'-'*60}\n{grupo} - {len(grupo)}")

print('\nDatos en forma de Tabla:')
print('-'*60)

for k in grupo[0].keys():
    print(f'{k:<13}', end='')
print('')

for alumno in grupo:
    for v in alumno.values():
        print(f'{v:<13}', end='')
    print('')

print('\nDatos en forma de Registro')
print('-'*60)

for est in grupo:
    for k, v in est.items():
        print(f'{k:<10} : {v}')
    print('')

print('\nCálculo de Promedios:')

suma_prom = sum(estudiante['Promedio'] for estudiante in grupo)
prom = suma_prom / len(grupo)

print(f'El promedio es {prom:.2f}')
print('finish')
