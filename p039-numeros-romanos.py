#-p039-numeros-romanos.py
print('\033[2J\033[H', end='')

print('Numero romanos')
num = int(input('Ingresa un numero del 1 al 10: '))

if num==1:
    print('I')
elif num==2:
    print('II')
elif num==3:
    print('III')
elif num==4:
    print('IV')
elif num==5:
    print('V')
elif num==6:
    print('VI')
elif num==7:
    print('VII')
elif num==8:
    print('VIII')
elif num==9:
    print('IX')
elif num==10:
    print('X')
else:
    print('FUERA DE RANGO')
print('FINISH')