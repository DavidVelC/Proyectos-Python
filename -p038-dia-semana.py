#-p038-dia-semana.py
print('\033[2J\033[H', end='')

dia = int(input('Ingresa un numero del 1 al 7: '))

if dia==1:
    print('Domigno')
elif dia==2:
    print('Lunes')
elif dia==3:
    print('Martes')
elif dia==4:
    print('Miercoles')
elif dia==5:
    print('Jueves')
elif dia==6:
    print('Viernes')
elif dia==7:
    print('Sabado')
else:
    print('Fuera de rango')
print('FINISH')