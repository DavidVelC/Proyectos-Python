#-p044-conteo-ascendente.py
#1 a n usando while
print('\033[2J\033[H', end='')
print('Imprime numeros de a n (100) con while')
c = 1
while c<=100:
    print(f'{c}', end=' ')
    c+=1
print('FINISH')