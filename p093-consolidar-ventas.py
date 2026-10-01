#p093-consolidar-ventas.py
# Consolidar las ventas de dos sucursales, usando listas
# Leer  ventas de cada día del mes 
# Dos sucursales, y guradar en dos listas separadas
# Añadir en tercera lista
print('\033[H\033[J')
print('Consolidar ventas de dos sucursales\n')
elementos = int(input('Ventas a registrar: '))

suc1 = []
suc2 = []
ventas_consolidadas = []

print('\nRegistrando ventas de la Sucursal 1: ')
for i in range(elementos):
    venta = int(input(f'Venta del día {i+1}: '))
    suc1.append(venta)
    
print('\nRegistrando ventas de la Sucursal 2: ')
for i in range(elementos):
    venta = int(input(f'Venta del día {i+1}: '))
    suc2.append(venta)

ventas_consolidadas = suc1 + suc2
print('Ventas consolidadas')
for i, venta in enumerate(ventas_consolidadas, start=1):
    print(f'Venta {i}: {venta}')
    
total = sum(ventas_consolidadas)
print('Total: ', total)