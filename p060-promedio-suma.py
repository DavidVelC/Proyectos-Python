#-p060-promedio-suma.py
while True:
    print('\033[H\033[J')
    suma = 0
    contador = 0
    print('Introduce numeros hasta el cero para sacar su promedio')
    while True:
        num = int(input('> '))
        if num==0:
            break
        suma+=num
        contador+=1
    promedio = suma/contador
    print('--------------------')
    print(f'Se introdujeron {contador} números.')
    print(f'La suma es: {suma}')
    print(f'El promedio es: {promedio}')    
    
    
    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break
print('finish')