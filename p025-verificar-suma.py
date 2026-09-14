#-p025-verificar-suma.py
#Verifica si la suma de dos numeros es igual a un tercero
print('Verifica si la suma de dos numeros es igual a un tercero')
n1 = int(input('Ingresa el primer numero: '))
n2 = int(input('Ingresa el segundo numero: '))
n3 = int(input('Ingresa el tercer numero: '))

if n1+n2 == n3:
    print(f'{n1+n2} y {n3} SON IGUALES!')
else: 
    print(f'{n1+n2} y {n3} SON DIFERENTES!')
print('FINISH')