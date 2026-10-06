#p103-resumen-ventas.py
print('\033[H\033[J')
print("\033[1;34m" + 'Actividad 14 Operaciones con matrices' + "\033[0m")

sales = [200, 300, 400, 500, 600, 1000, 2000]
sales_desc = [v * 0.9 if v > 1000 else v * 0.95 for v in sales]

sales_rel = [v for v in sales_desc if v > 500]

print('Ventas originales: ', sales)
print('Ventas con descuento: ', sales_desc)
print('Ventas relevantes (mayores a 500): ', sales_rel)
