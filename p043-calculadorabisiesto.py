# p043-calculadora-anio-bisiesto.py

print('Cumpleaños en año bisiesto')

year = int(input('Ingresa tu año de nacimiento: '))

if year % 4 == 0 and year % 100 != 0:
    print('Fue año bisiesto')
elif year % 400 == 0:
    print('Fue año bisiesto')
else:
    print('No fue año bisiesto')
print('Finish')