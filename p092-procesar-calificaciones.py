#p092-procesar-calificaciones.py
# Procesa calificaciones en una lista
# Al final muestra la lista, suma, promedio, la mas alta y la mas baja

print('\033[H\033[J')
print('Procesador de calificaciones de un curso\n')
print("Introduce calificaciones entre 0 y 10 (usa 99 para terminar):\n")

calif = []
suma = 0.0

while True:
    try:
        n = float(input("Calificación > "))

        if n == 99:
            break

        if 0 <= n <= 10:
            calif.append(n)
            suma += n
        else:
            print("Error: la calificación debe estar entre 0 y 10.")

    except ValueError:
        print("DEBES INGRESAR SOLO NUMEROS")


if calif:
    prom = suma / len(calif)
    max_calif = max(calif)
    min_calif = min(calif)
    sup_prom = sum(1 for cal in calif if cal > prom)

    print('\nResultados')
    print(f'Lista de calificaciones: {calif}')
    print(f'Suma de calificaciones: {suma}')
    print(f'Promedio de calificaciones: {prom:.2f}')
    print(f'Calificación máxima: {max_calif}')
    print(f'Calificación mínima: {min_calif}')
    print(f'Calificaciones mayores al promedio: {sup_prom}')

else:
    print("No se ingresaron calificaciones.")

print('Proceso finalizado')