# p091-gestionar-gastos.py
# Gestionar una lista de gastos mensuales

print('\033[H\033[J')  # Limpiar pantalla
print('Gestionar una lista de gastos mensuales')

gastos = [500, 1200, 350, 800, 150]

salir = False

while salir == False:

    print('\n========== MENU DE OPCIONES ==========')
    print('1. Ver Gastos')
    print('2. Agregar Gasto')
    print('3. Modificar Gasto')
    print('4. Eliminar Gasto')
    print('5. Ver Total')
    print('6. Salir')
    print('======================================')

    try:
        opcion = int(input('Selecciona una opcion: '))

        # Ver gastos
        if opcion == 1:

            print('\n--- GASTOS ACTUALES ---')

            if len(gastos) == 0:
                print('No hay gastos registrados')
            else:
                for i in range(len(gastos)):
                    print(f'Indice: {i} | Gasto: ${gastos[i]:.2f}')

                print(f'Total de gastos registrados: {len(gastos)}')


        # Agregar gasto
        elif opcion == 2:

            try:
                gasto = float(input('\nIngresa el monto del nuevo gasto: $'))

                if gasto < 0:
                    print('Error: El gasto no puede ser negativo')
                else:
                    gastos.append(gasto)
                    print(f'Gasto de ${gasto:.2f} agregado correctamente')

            except ValueError:
                print('Error: Debes introducir un numero')


        # Modificar gasto
        elif opcion == 3:

            if len(gastos) == 0:
                print('\nNo hay gastos para modificar')
            else:

                print('\n--- GASTOS ACTUALES ---')

                for i in range(len(gastos)):
                    print(f'Indice: {i} | Gasto: ${gastos[i]:.2f}')

                try:
                    indice = int(input('\nIngresa el indice del gasto que deseas modificar: '))

                    if indice >= 0 and indice < len(gastos):

                        try:
                            nuevo_gasto = float(
                                input('Ingresa el nuevo valor del gasto: $')
                            )

                            if nuevo_gasto < 0:
                                print('Error: El gasto no puede ser negativo')
                            else:
                                gastos[indice] = nuevo_gasto
                                print('Gasto modificado correctamente')

                        except ValueError:
                            print('Error: Debes introducir un numero')

                    else:
                        print('Gasto no encontrado')

                except ValueError:
                    print('Error: El indice debe ser un numero entero')


        # Eliminar gasto
        elif opcion == 4:

            if len(gastos) == 0:
                print('\nNo hay gastos para eliminar')
            else:

                print('\n--- GASTOS ACTUALES ---')

                for i in range(len(gastos)):
                    print(f'Indice: {i} | Gasto: ${gastos[i]:.2f}')

                try:
                    indice = int(input('\nIngresa el indice del gasto que deseas eliminar: '))

                    if indice >= 0 and indice < len(gastos):

                        gasto_eliminado = gastos[indice]
                        del gastos[indice]

                        print(
                            f'Gasto de ${gasto_eliminado:.2f} eliminado correctamente'
                        )

                    else:
                        print('Gasto no encontrado')

                except ValueError:
                    print('Error: El indice debe ser un numero entero')


        # Ver total
        elif opcion == 5:

            total = sum(gastos)

            print('\n--- TOTAL DE GASTOS ---')
            print(f'Total gastado: ${total:.2f}')


        # Salir
        elif opcion == 6:

            print('\nSaliendo del programa...')
            print('Programa terminado')
            salir = True


        # Opcion incorrecta
        else:

            print('\nError: Opcion no valida')

    except ValueError:

        print('\nError: Debes introducir un numero entero para seleccionar una opcion')
print('Programa finalizado')