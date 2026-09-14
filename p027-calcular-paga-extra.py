#-p027-calcular-paga-extra.py
#Calcula la paga de un trabajador considerando horas extras
print('Calcula la paga de un trabajador considerando horas extras')
print('Ingresa tus datos')
name = input('Nombre: ')
horas = int(input('Horas trabajadas: '))
pago_hora = float(input('Paga/hora: '))

turno = 40
pagoT = turno*pago_hora
horas_extra = pago_extra = 0
if horas>40:
    horas_extra = horas-40
    pago_extra = horas_extra*(pago_hora*2)
    total = pagoT+pago_extra
else: 
    pagoT = horas*pago_hora
total = pagoT
    
print(f'{name} trabajó {horas} en la semana')
print(f'Pago normal: {pagoT}')
print(f'Horas extra: {horas_extra}')
print(f'Pago extra: {pago_extra}')
print(f'Total: {total}')