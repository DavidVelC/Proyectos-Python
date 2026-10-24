#p130-conjunto-personas.py
print('\033[H\033[J')

lista1 = ['Juan', 'Maria', 'Pedro', 'Jose', 'Rocio']
lista2 = ['Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther']

A = set(lista1)
B = set(lista2)

print('Conjuntos base:')
print(f'A: {A}')
print(f'B: {B}')

# Operacione
print('\nUnion de conjuntos')
print(f'A | B: {A | B}')

print('\nInterseccion de conjuntos')
print(f'A & B: {A & B}')

print('\nDiferencia de conjuntos')
print(f'A - B: {A - B}')

print('\nDiferencia simetrica de conjuntos')
print(f'A ^ B: {A ^ B}')

print('\nVerificacion de afirmaciones')
subconjunto = {"Pablo", "Mateo"}
print(f'¿{{Pablo, Mateo}} es subconjunto de B? {subconjunto.issubset(B)}')
print(f'¿A es superconjunto de {{Reynaldo, Angelica}}? {A.issuperset({"Reynaldo", "Angelica"})}')

print(f'¿Pedro esta en A? {"Pedro" in A}')

print(f'¿Lilia no esta en B? {"Lilia" not in B}')

print('\nFIsnish')
