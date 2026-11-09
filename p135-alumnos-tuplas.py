
# p135-registro-alumnos-tuplas.py
# Registro escolar utilizando tuplas anidadas

alumnos = (
    ("Ana", "ISC", (9, 10, 9, 8)),
    ("Luis", "ISW", (8, 8, 9, 10)),
    ("Mar", "ISC", (10, 9, 10, 10))
)

# Mostrar la tupla completa
print("Registro escolar:")
print(alumnos)
print("Total de alumnos:", len(alumnos))

# calcular prom de alumnos
print("\nPromedios de los alumnos:")

for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre} - {carrera} - Promedio: {promedio:.2f}")

# Construir una nueva tupla con pares (nombre, promedio).
promedios = tuple(
    (nombre, sum(calificaciones) / len(calificaciones))
    for nombre, carrera, calificaciones in alumnos
)

print("\nTupla de promedios:")
print(promedios)

# Identificar al alumno con el promedio mas alto.
mejor_alumno = promedios[0]

for alumno in promedios:
    if alumno[1] > mejor_alumno[1]:
        mejor_alumno = alumno

print(f"Alumno con el promedio mas alto: {mejor_alumno[0]} ({mejor_alumno[1]:.2f})")

# Consultar las calificaciones utilizando indices de tuplas anidadas.
print("\nConsulta de calificaciones:")

for alumno in alumnos:
    nombre = alumno[0]
    calificaciones = alumno[2]

    # count() cuenta cuantas veces aparece el numero 10.
    cantidad_diez = calificaciones.count(10)

    # index() devuelve la posicion de la primera aparicion del numero 10.
    posicion_diez = calificaciones.index(10)

    print(f"{nombre}: Calificaciones: {calificaciones}")
    print(f"  Cantidad de veces que aparece 10: {cantidad_diez}")
    print(f"  Primera posicion del 10: {posicion_diez}")

promedios_ordenados = tuple(sorted(promedios, key=lambda alumno: alumno[1]))

print("\nPromedios ordenados de menor a mayor:")
print(promedios_ordenados)

#nueva tupla
nuevo_alumno = ("Eva", "ISC", (9, 9, 10))

print("\nNuevo registro de alumno:")
print(nuevo_alumno)

print("\nTupla original de alumnos sin cambios:")
print(alumnos)

print("\nProceso finalizado")
