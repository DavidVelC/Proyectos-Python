# p051-adivina-numero.py

import random

print('\033[2J\033[H', end='')
print('Adivina el numero ')
print('He pensado un numero entre 1 y 50, adivina cual es')

ns = random.randint(1,50)
ci = 0

while True:
    intento = int(input('Cual es ? '))
    ci += 1

    if intento < ns:
        print('Demasiado bajo intenta con un numero mas alto')
    elif intento > ns:
        print('Demasiado alto intenta con un numero mas bajo')
    else:
        print(f'Felicidades Adivinste el numero en {ci} intentos')
        print('El numero era : ', ns)
        break

print('\n Terminamos Gracias')