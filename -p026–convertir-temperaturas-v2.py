#-p026–convertir-temperaturas-v2.py
#Conversor celsius- farenheit y viceversa

print('Conversor celsius- farenheit y viceversa')
print('[1] Farenheit a Celsiuis')
print('[2] Celsius a Farenheit')
op = int(input('Ingresa tu selección: '))

if op == 1:
    print('Farenheit a Celsius')
    faren = float(input('Ingresa la temperatura en farenheit: '))
    celsius = (faren-32)*(5/9)
    print('La temperatura es: ' +str(celsius))
else:
    if op == 2:
        print('Celsius a Farenheti')
        celsius = float(input('Ingresa la temperatura en celsius: '))
        faren = (celsius*9/5)+32
        print('La temperatura es: ' +str(faren))
    else:
        print('Opción invalida')
print('Finish')