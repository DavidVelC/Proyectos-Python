#-p061-suma-200.py
while True:
    print('\033[H\033[J')
    suma = 0
    cont = 0
    print('Introduce numeros hasta alcanzar 200')
    while suma<200:
        num = int(input(f'Suma actual {suma}. Intruduce un numero: '))
        suma+=num
        cont+=1
    print('--------------------')
    print(f'Meta de 200 alcanzada')
    print(f'La suma es: {suma}')
    print(f'Numeros introducidos: {cont}')    
    
    
    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break
print('finish')