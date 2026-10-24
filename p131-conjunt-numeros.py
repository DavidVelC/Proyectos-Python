#p131-conjunt-numeros.py
print('\033[H\033[J')

lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(lista1)
B = set(lista2)
C = set(lista3)

print('Conjuntos base:')
print(f'A: {A}')
print(f'B: {B}')
print(f'C: {C}')

print('\nUnion de conjuntos')
print(f'A | B: {A | B}')
print(f'B | C: {B | C}')

print('\nDiferencia de conjuntos')
print(f'A - C: {A - C}')

print('\nDiferencia simetrica de conjuntos')
print(f'B ^ C: {B ^ C}')

print('\nInterseccion de conjuntos')
print(f'B & C: {B & C}')

print('\nVerificacion de afirmaciones')

print(f'¿A es subconjunto de B? {A.issubset(B)}')
print(f'¿C es subconjunto de A? {C.issubset(A)}')
print(f'¿El numero 100 esta en A? {100 in A}')
print(f'¿El numero 60 esta en A, B y C? {60 in A and 60 in B and 60 in C}')
print(f'¿El numero 900 no esta en C? {900 not in C}')

print('\nProceso finalizado')
