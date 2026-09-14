#p058-impares-ascendente.py
#imprime los numeros impare de forma ascendente en una lista y la suma de todo
while True:
    print('\033[H\033[J')
    print("Imprime los numeros impares de forma ascendente")
    n = int(input('Introduce hasta que numero contar: '))
    num=[]
    c=1
    while c<n:
        if c%2!=0:
            imp=c
            num.append(imp)
        c+=1
    total = sum(num)
    print(f'\nLista de números impares: {num}')   
    print(f'La suma de todos los números es: {total}')  
    
    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break
print('finish')