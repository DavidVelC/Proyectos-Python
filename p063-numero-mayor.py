#-p063-numero-mayor.py
#-p061-suma-200.py
while True:
    print('\033[H\033[J')
    mayor = 0
    print('Introduce numeros hasta alcanzar el mayor (ingresa cero para terminar)')
    while True:
        num = int(input('> '))
        if num==0:
            break
        if num>mayor:
            mayor=num
    print('-'*40)
    print(f'el mayor fue {mayor}')
    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break
print('finish')