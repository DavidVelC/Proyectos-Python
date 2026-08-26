#p028-retira-cuenta.py
#simula el retiro de una cuenta

saldo = 1500.00
print('Simula retiro de dinero de una cuenta')

retiro = float(input(f'Cantidad a retirar de la cuenta || Saldo actual: {saldo}'))
if retiro>0 and retiro<saldo:
    print('Procedemos')
    if retiro<=saldo:
        saldo = saldo-retiro
        print(f'Retiro exitoso || Saldo actual {saldo}')
    else:
        print('Saldo insuficiente')
else:
    print('Debe ser un numero positivo')
