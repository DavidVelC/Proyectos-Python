#p146-numero-mayor.py
def numero_mayor(n1: int, n2: int, n3: int) -> int:
    mayor = n1
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 >n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3

print('Dame tres numeros enteros separados por enter:')
a, b, c = int(input()), int(input()), int(input())
print(f'El número mayor es: {numero_mayor(a, b, c)}')