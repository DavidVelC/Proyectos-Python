#p094-precio-acciones.py
# p094-precio-acciones.py
# Análisis básico de protafoio de acciones
print('\033[H\033[J')
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
precios = []
for i in range (1,8):
    precio = float(input('Ingresa un precio (solo dentro de la semana): '))
    #precios = [150.25, 152.50, 149.75, 155.00, 153.20]
    precios.append(precio)
    
precio_max = max(precios)
precio_min = min(precios)

pos_max = precios.index(precio_max)
pos_min = precios.index(precio_min)
print(f"\nPrecios de la semana: {precios}")
print(f"El precio más alto fue ${precio_max} el día {dias[pos_max]}.")
print(f"El precio más bajo fue ${precio_min} el día {dias[pos_min]}.")