#- p077-factorial-numeros.py
print('\033[2J\033[H', end='')
print('Factorial')

try: 
    n = int(input('Factorial'))
    print(f'{n}! = ', end='')
    f=1
    for x in range (1, n+1):
        print(f'{x}! = ', end='')
        f=1
        for i in range (1, n+1):
            print(f'{i}{' x ' if i<n else ''}', end='')
except ValueError:
    print('Solo numero enteros')   