# p004-paga-trabajador.py
# Calcular la paga total de un trabajador

print('Calcula la paga de un trabajador')
nombre = input("Nombre: ")
horas = int(input("Horas trabajadas: "))
paga = float(input("Paga por hora: "))
tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto
print("\nResumen de pagos:".center(20))
print(f"El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga} pesos por hora, impuesto de {tasa}%")
print(f"{"Pago bruto:":<12}{pagabruta}")
print(f"{"Impuesto:":<12}{impuesto}")
print(f"{"Paga neta:":<12}{paganeta}")