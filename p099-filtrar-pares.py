#p099-filtrar-pares.py
#Filtra los numeros pares
print('\033[H\033[J')
print("\033[1;32m" + 'Actividad 14 FIltrar los numeros pares' + "\033[0m")

n = int(input('Cantidad de numeros a introducir: '))
numList = []

for i in range(n):
    num = int(input(f'Ingrese el numero: {i+1}: '))
    numList.append(num)
    
#filtrar
pares = [x for x in numList if x%2 == 0]
impares = [x for x in numList if x%2 != 0]
print(f'Numeros introducidos: {numList}')
print(f'Numeros pares: {pares} - cantidad {len(pares)}')
print(f'Numeros impares: {impares} - cantidad {len(impares)}')