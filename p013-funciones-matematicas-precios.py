#-p013-funciones-matematicas-precios.py 

#Funciones matematicas de redondeo
import math as mt
print('\033[2J\033\[H', end='')

precio = float(input("\nIngresa un precio: ")) #con valor decimal
# metodos de redondeo
arriba = mt.ceil(precio)
abajo = mt.floor(precio)
truncado = mt.trunc(precio)
redondeo = round(precio)
un_decimal = round(precio, 1)


print(f"Precio original. : ${precio}")
print(f"Redondeo arriba (ceil): ${arriba}")
print(f"Redondeo abajo (floor): ${abajo}")
print(f"Truncado (trunc) : ${truncado}")
print(f"Redondeo normal : ${redondeo}")
print(f"Redondeo 1 decimal : ${un_decimal}")