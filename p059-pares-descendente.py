#-p059-pares-descendente.py
#imprime los numeros pares de forma descendente en una lista y la suma de todo
while True:
    #print('\033[H\033[J')
    print("Imprime los numeros pares de forma descendente")
    n = int(input('Introduce hasta que numero contar (menor a 100): '))
    num=[]
    c=100
    while c>=n:
        if c%2==0:
            par=c
            num.append(par)
        c-=1
    total = sum(num)
    print(f'\nLista de números pares: {num}')   
    print(f'La suma de todos los números es: {total}')  
    
    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break
print('finish')