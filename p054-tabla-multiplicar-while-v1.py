#-p054-tabla-multiplicar-while-v1.py
while True:
    print('Imprime la secunecia de collatz')
    print('Imprime la tabla del 1 al 10 usando while\n')

    t = int(input('De que numero: '))
    n = int(input('QUe rango: '))
    print('Imprime tabla de ' +str(t))
    c=1
    while c<=n:
        print(f'{t:3} x {c:3} = {c*t}')
        c+=1
    if input('Deseas Continuar (S/N)? ').upper()=='N': 
        break
print('FINISH')