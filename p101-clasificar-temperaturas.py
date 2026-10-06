#p101-clasificar-temperaturas.py
#claifica temperaturas en fria, templada y caliente
print('\033[H\033[J')
print("\033[1;34m" + 'Actividad 14 Claisificación de temperatura' + "\033[0m")

temp = [15, 22, 30, 10, 25, 18, 35, 28]
clasif = [
    'Fria' if t < 20 else
    'Templada' if t <= 30 else
    'Caliente' for t in temp
]

print('Temperaturas: ', temp)
print('Clasificacion: ', clasif)