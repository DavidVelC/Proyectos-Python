# p096-procesar-datos-sensores.py
# Simulación de recolección y procesamiento de datos de sensores
# genera datos smuladios    
from random import randint
print('\033[H\033[J')
print("Simulando la recolección de datos de dos sensores...")
sensor1 = []
sensor2 = []
mediciones = int(input('Ingresa el numero de mediciones: '))
for _ in range(mediciones):
    sensor1.append(randint(1, 100))
    sensor2.append(randint(1, 100))
print('Datos de los sensores')
print(f"Sensor A: {sensor1}")
print(f"Sensor B: {sensor2}")

datos_combinados = []
for i in range(mediciones):
    sensor1[i] = sensor1[i] ** 2
    sensor2[i] = sensor2[i] ** 2
suma_transformada = sensor1[i] + sensor2[i]
#datos_combinados.append(suma_transformada)
print("\nDatos Procesados")
print(f"Sensor 1 (Transformados): {sensor1}")
print(f"Sensor 2 (Transformados): {sensor2}")

total = []
for i in range (mediciones):
    total.append(sensor1[i] + sensor2[i])
print(f"Datos Combinados: {total}")