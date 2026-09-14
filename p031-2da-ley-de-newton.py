#-p031-2da-ley-de-newton.py
#
print('Calculadora de la 2da Ley de Newton')
print('F = m*a')
print('[1] Calcular la Fuerza (fuerza = masa * aceleración)')
print('[2] Calcular la Masa (masa = fuerza / aceleración)')
print('[3] Calcular la Aceleración (aceleración = fuerza / masa)')
opc = int(input('Ingresa tu slección'))

if opc == 1:
    print('\n Calculando Fuerza...')
    m = float(input('Masa: '))
    a = float(input('Aceleración: '))
    f = m*a
    print(f' La fuerza es: {f} ')
elif opc == 2:
    print('\n Calculando la Masa...')
    f = float(input('Fuerza: '))
    a = float(input('Aceleración: '))
    m = f/a
    print(f' La masa es: {m} ')
elif opc == 3:
    print('\n Calculando la Aceleración...')
    f = float(input('Fuerza: '))
    m = float(input('Masa: '))
    a = f/m
    print(f' La aceleración es: {a} ')

else:
    print('Np es una opciín disponible')
