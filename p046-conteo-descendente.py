#-p046-conteo-descendente.py
#conteo descendente
print('\033[2J\033[H', end='')
print('Imprime numeros de 100 a n 0 con while')
c = 100
while c>1:
    print(c, end=' ')
    c-=1
print('FINISH', c)