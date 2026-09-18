#p081-plan-ahorro-depistos-mensuales.py
print('\033[2J\033[H', end='')
print('Plan de ahorro')

saldo = float(input('Monto inicial: '))
deposito = float(input('Deposito mensual: '))
tasa = float(input('Tasa de interes mensual (%): '))
meses = int(input('Numero de meses: '))

print('\nMes\tSaldo inicial\tInteres\t\tSaldo final')
print('----------------------------------------------------------')

for mes in range(1, meses + 1):
    saldo_inicial = saldo
    interes = saldo_inicial * tasa / 100
    saldo = saldo_inicial + interes + deposito

    print(f'{mes}\t${saldo_inicial:.2f}\t\t${interes:.2f}\t\t${saldo:.2f}')

print('\nProceso Terminado')