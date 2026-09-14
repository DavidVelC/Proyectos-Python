#-p036-numeros-consecutivos.py
# Leer tres números enteros con Enter
print('\033[2J\033[H', end='')
print('Determina si son numeros consecutivos')
print("Ingresa 3 numeros separado por un espacio")

n1, n2, n3 = input().split()
n1, n2, n3 = [ int(n1), int(n2), int(n3) ]

if n2==(n1+1) and n3==(n2+1):
    print(f'{n1}, {n2}, {n3} si son consecutivos')
else:
    print(f'{n1}, {n2}, {n3} no son consecutivos')
print('finish')