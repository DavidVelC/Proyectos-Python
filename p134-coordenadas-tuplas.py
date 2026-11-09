
# p134-coordenadas-tuplas.py
# Registro de coordenadas geograficas utilizando tuplas

# Definicion de las tuplas con los datos de cada ciudad
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

# Mostrar las tuplas y consultar su tipo
print("Tupla Zacatecas:", zacatecas, ", Tipo:", type(zacatecas))
print("Tupla Guadalupe:", guadalupe, ", Tipo:", type(guadalupe))

# Acceso a los elementos mediante indices positivos y negativos
print("\nAcceso por indices (Zacatecas):")
print(f"  Positivos -> Nombre: {zacatecas[0]}, Latitud: {zacatecas[1]}, Longitud: {zacatecas[2]}")
print(f"  Negativos -> Nombre: {zacatecas[-3]}, Latitud: {zacatecas[-2]}, Longitud: {zacatecas[-1]}")

# Desempaquetado de las tuplas en variables
nombre_zac, lat_zac, lon_zac = zacatecas
nombre_gua, lat_gua, lon_gua = guadalupe

# Mostrar las coordenadas utilizando el formato solicitado
print(f"{nombre_zac}: ({lat_zac}, {lon_zac})")
print(f"{nombre_gua}: ({lat_gua}, {lon_gua})")

# Recorrer ambas ubicaciones utilizando un ciclo
print("\nRecorrido de ubicaciones:")

for lugar in [zacatecas, guadalupe]:
    # El slicing [1:] obtiene los elementos desde el indice 1 hasta el final.
    # De esta manera se obtiene una tupla con la latitud y longitud.
    print(f"Ubicacion: {lugar[0]}, Coordenadas: {lugar[1:]}")

# Calcular el punto medio aproximado entre las dos ubicaciones
# Se obtiene el promedio de las latitudes y de las longitudes.
punto_medio = ((lat_zac + lat_gua) / 2, (lon_zac + lon_gua) / 2)

print(f"Punto medio aproximado: ({punto_medio[0]:.2f}, {punto_medio[1]:.2f})")

# Crear una nueva tupla agregando el codigo ZAC
# El operador + permite concatenar tuplas, sin modificar la original.
nueva_zacatecas = zacatecas + ("ZAC",)

print("Nueva tupla Zacatecas:", nueva_zacatecas)

# Comprobar que la tupla original permanece sin cambios
print("Original sin cambios:", zacatecas)

# Verificar pertenencia de un elemento en la tupla
print("'Zacatecas' pertenece a la tupla:", "Zacatecas" in zacatecas)

# Las tuplas son inmutables, por lo que no se puede reemplazar
# directamente uno de sus elementos.
# Por ejemplo: zacatecas[0] = "Otra ciudad" generaria un TypeError.
