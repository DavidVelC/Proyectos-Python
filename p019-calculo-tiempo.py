#-p019-calculo-tiempo.py
#tome una cantidad de horas como un número entero.
print('Calcula las horas en dias, minutos y segundos\n')

horas = float(input('Ingresa las horas: '))

dia = horas*(1/24)
min = horas*60
seg = horas*3600

temp = ('Resultados\n'
        f'Dias: {dia:.2f}\n'
        f'Minutos: {min:.2f}\n'
        f'Segundos: {seg:.2f}\n')
print(temp)