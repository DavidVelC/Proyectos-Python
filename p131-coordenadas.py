#p131-coordenadas.py
# p132-coordenadas.py
# Registro de coordenadas geográficas usando tuplas

# Definición de tuplas para las coordenadas de dos ciudades
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

# Acceso a los elementos de la tupla usando índices
print("Coordenadas de Zacatecas:")
print("Tipo      : ", type(zacatecas))
print("Ciudad    : ", zacatecas[0])
print("Latitud   : ", zacatecas[1])
print("Longitud  : ", zacatecas[2])

ciudad, latitud, longitud = guadalupe
print("\nCoordenadas de Guadalupe:")
print("Tipo      : ", type(guadalupe))
print("Ciudad    : ", ciudad)
print("Latitud   : ", latitud)
print("Longitud  : ", longitud)

nombre, lat, lon = zacatecas
print(f"{nombre}: ({lat}, {lon})")

for lugar in [zacatecas, guadalupe]:
    print("\nCoordenadas de", lugar[0])
    print("Latitud  : ", lugar[1])
    print("Longitud : ", lugar[2])

# Desempaquetado ignora el primer elemento (nombre de la ciudad) y obtiene las coordenadas
_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe

# Calculo del punto medio entre las dos coordenadas
centro = ((lat1 + lat2) / 2, (lon1 + lon2) / 2)
print("Punto medio ", centro)

# Verificar pertenencia
print("Zacatecas pertenece a la tupla: ", "Zacatecas" in zacatecas)

# Crear otra tupla con las coordenadas de otra ciudad
ampliada = zacatecas + ("ZAC",)
print("Ampliada:", ampliada)
print("Original:", zacatecas)

print('finish')