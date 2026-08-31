#imprime a 1 en intervalos de m
print('\033[2J\033[H', end='')
print('Imprime numeros de a n (100) con while')
n = int(input('Ingresa el numero: '))
m = int (input('Incrementos: '))
#c = 1
while c<=n:
    print(c, end=' ')
    c-=m
print('FINISH')