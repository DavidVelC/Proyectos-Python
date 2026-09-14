#-p024-verificar-numero-v2.py
print('Verificar si un numero entero es positivo, negativo o cero')
num = int(input('Ingresa el numero: '))

if num == 0:
    print('Es cero!')
else:
    if num>0:
        print('El numero es positivo!')
    else:
        if num<0: 
            print('El numero es negativo!')