#p106-mes-día-nombre.py
# Mostrar el nombre y la cantidad de dias de un mes

print('\033[H\033[J')
print('Consulta de dias por mes\n')

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = int(input('Introduce el numero del mes (1-12): '))

if 1 <= n <= 12:
    print(f'\nMes: {meses[n-1]}')
    print(f'Cantidad de dias: {dias[n-1]}')
else:
    print('Error: introduce un numero entre 1 y 12.')