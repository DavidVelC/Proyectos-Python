#p136-AeroRegistro

# AeroRegistro.py
# Registro y procesamiento de vuelos de una aerolinea

# Inicializamos la lista vacia para almacenar todos los vuelos.
# Cada elemento de esta lista sera un diccionario.
registro_vuelos = []

print("--- Captura de Datos del Vuelo ---")
print("(Deje el numero de vuelo vacio o ingrese '*' para finalizar la captura)\n")

# Ciclo while para capturar tantos vuelos como el usuario necesite.
while True:
    numero_vuelo = input("Numero de vuelo (ej. AA-101): ")

    # Si el usuario no escribe nada o introduce '*', termina la captura.
    if numero_vuelo == "" or numero_vuelo == "*":
        break

    origen = input("Ciudad de origen (ej. Ciudad de Mexico): ")
    destino = input("Ciudad de destino (ej. Guadalajara): ")
    aerolinea = input("Nombre de la aerolinea (ej. Volaris): ")
    pasajeros = int(input("Numero de pasajeros a bordo: "))
    tarifa = float(input("Tarifa del boleto en pesos: "))

    # Creamos un diccionario para almacenar los datos del vuelo actual.
    vuelo = {
        "numero_vuelo": numero_vuelo,
        "origen": origen,
        "destino": destino,
        "aerolinea": aerolinea,
        "pasajeros": pasajeros,
        "tarifa": tarifa
    }

    # append() agrega el diccionario al final de la lista principal.
    registro_vuelos.append(vuelo)
    print("-> Vuelo registrado exitosamente.\n")

print("\n=============================================")
print("             DATOS EN PANTALLA               ")
print("=============================================")

# --- 1. IMPRESION DE DATOS CRUDOS ---

# Mostramos la lista completa de diccionarios tal como fue almacenada.
print("\nDATOS CRUDOS DEL REGISTRO DE VUELOS:")
print(registro_vuelos)


# --- 2. VISUALIZACION DE CONJUNTOS Y TUPLAS ---

# Creamos un conjunto a partir de los destinos de cada vuelo.
# set() elimina automaticamente los elementos repetidos.
destinos_unicos = set()

for v in registro_vuelos:
    destinos_unicos.add(v["destino"])

print("\nLISTA DE VUELOS Y DESTINOS:")
print(f"Conjunto de destinos unicos: {destinos_unicos}")

# Creamos una lista para almacenar el registro historico.
# Cada elemento sera una tupla con numero de vuelo, aerolinea y destino.
registro_historico = []

for v in registro_vuelos:
    registro_historico.append((v["numero_vuelo"], v["aerolinea"], v["destino"]))

print(f"Registro historico: {registro_historico}")


# --- 3. FORMATO DE TABLA TABULAR ALINEADA ---

print("\nREPORTE TABULAR DE VUELOS:")

# El simbolo < alinea el texto a la izquierda dentro del espacio indicado.
# El simbolo > alinea el texto a la derecha.
encabezado = f"{'VUELO':<10} | {'ORIGEN':<20} | {'DESTINO':<20} | {'AEROLINEA':<15} | {'PASAJEROS':<10} | {'TARIFA':<12}"

print(encabezado)
print("-" * len(encabezado))

# Recorremos los diccionarios para mostrar cada vuelo en una fila.
for v in registro_vuelos:
    # :.2f muestra la tarifa con dos decimales.
    tarifa_formateada = f"${v['tarifa']:.2f}"

    fila = f"| {v['numero_vuelo']:<10} | {v['origen']:<20} | {v['destino']:<20} | {v['aerolinea']:<15} | {v['pasajeros']:>10} | {tarifa_formateada:>12} |"

    print(fila)

print("-" * len(encabezado))


# --- 4. RESUMEN ESTADISTICO DE AEROREGISTRO ---

print("\nRESUMEN ESTADISTICO:")

# len() devuelve la cantidad de elementos de la lista.
total_vuelos = len(registro_vuelos)

print(f"Total de vuelos registrados: {total_vuelos}")

# Estos diccionarios funcionaran como contadores.
# Las llaves seran las aerolineas y los destinos.
# Los valores indicaran cuantas veces aparece cada uno.
conteo_aerolineas = {}
conteo_destinos = {}

for v in registro_vuelos:
    aero = v["aerolinea"]
    dest = v["destino"]

    # Si la aerolinea no existe como llave, se agrega con valor 1.
    # Si ya existe, se incrementa su contador.
    if aero not in conteo_aerolineas:
        conteo_aerolineas[aero] = 1
    else:
        conteo_aerolineas[aero] += 1

    # Aplicamos el mismo procedimiento para los destinos.
    if dest not in conteo_destinos:
        conteo_destinos[dest] = 1
    else:
        conteo_destinos[dest] += 1

print("\nVuelos por Aerolinea:")

# items() permite obtener simultaneamente la llave y su valor.
for nombre_aero, cantidad in conteo_aerolineas.items():
    print(f" - {nombre_aero}: {cantidad} vuelo(s)")

print("\nVuelos por Ciudad de Destino:")

for nombre_dest, cantidad in conteo_destinos.items():
    print(f" - {nombre_dest}: {cantidad} vuelo(s)")


# --- 5. OPERACIONES, ACUMULADORES Y EXTREMOS ---

print("\nANALISIS FINANCIERO Y OPERATIVO:")

# Comprobamos que existan vuelos para evitar divisiones entre cero.
if total_vuelos > 0:

    # Inicializamos acumuladores para sumar pasajeros y tarifas.
    suma_pasajeros = 0
    suma_tarifas = 0

    # Inicializamos las variables en None.
    # None representa que todavia no tienen un vuelo asignado.
    vuelo_caro = None
    vuelo_barato = None

    # Recorremos todos los vuelos para realizar los calculos.
    for v in registro_vuelos:

        # Acumulamos los pasajeros y las tarifas de cada vuelo.
        suma_pasajeros += v["pasajeros"]
        suma_tarifas += v["tarifa"]

        # Si no hay un vuelo caro asignado, se toma el primero.
        # Despues se compara la tarifa de cada vuelo.
        if vuelo_caro is None or v["tarifa"] > vuelo_caro["tarifa"]:
            vuelo_caro = v

        # Se aplica el mismo procedimiento para encontrar
        # el vuelo con la tarifa mas baja.
        if vuelo_barato is None or v["tarifa"] < vuelo_barato["tarifa"]:
            vuelo_barato = v

    # Calculamos los promedios dividiendo entre el total de vuelos.
    promedio_pasajeros = suma_pasajeros / total_vuelos
    promedio_tarifa = suma_tarifas / total_vuelos

    # Mostramos los resultados con dos decimales cuando corresponde.
    print(f"Suma total de pasajeros: {suma_pasajeros}")
    print(f"Promedio de pasajeros por vuelo: {promedio_pasajeros:.2f}")
    print(f"Suma total de tarifas: ${suma_tarifas:.2f}")
    print(f"Tarifa promedio general: ${promedio_tarifa:.2f}")

    print(f"Vuelo mas caro: Numero {vuelo_caro['numero_vuelo']} con una tarifa de ${vuelo_caro['tarifa']:.2f}")

    print(f"Vuelo mas barato: Numero {vuelo_barato['numero_vuelo']} con una tarifa de ${vuelo_barato['tarifa']:.2f}")

else:
    # Mensaje mostrado cuando no se registro ningun vuelo.
    print("No se registraron vuelos. No es posible calcular totales, promedios ni extremos.")

print("\nProceso finalizado")
