#-p067-gasolinera.py
#Sistema de gestion de una estacion de servicio
#While mantiene el programa ejecutandose mientras sea TRUE
while True:
    print('\033[2J\033[H', end='')#limpiar pantalla al inicio del programa

    print('======================================')
    print('       ESTACION DE SERVICIO')
    print('======================================')
    print('[ 1 ] Venta de combustible')
    print('[ 2 ] Simulacion de rendimiento')
    print('[ 3 ] Clasificador de cliente')
    print('[ 4 ] Salir')
    print('======================================')

    op = int(input('Elige una opcion: '))

    # VENTA DE COMBUSTIBLE
    if op == 1:

        print('\n--- VENTA DE COMBUSTIBLE ---')
        print('- Magna: $23.68/L\n- Premium: $28.49/L\n- Diesel: $27.00/L\n')
        mag = 23.68
        prem = 28.49
        dis = 27.00
        combustible = input('Tipo de combustible: ')
        combustible = combustible.upper()#volver mayusculas
        #precio = float(input('Precio por litro: '))# instruccion innecesaria
        #mejor precios como constante que como variable
        precio = 0
        litros = float(input('Cantidad de litros: '))

        if precio < 0 or litros <= 0:
            print('\nError: el precio y los litros deben ser positivos.')
            continue
        elif combustible == 'MAGNA':
            precio=mag
        elif combustible == 'PREMIUM':
            precio = prem
        elif combustible == 'DISEL' or 'DIESEL':
            precio = dis
        else:#mecanismos de control para reducir errores
            print('No es una opción válida')
        total = precio * litros

        print('\n--------------------------------------')
        print(f'Combustible:  {combustible}')
        print(f'Precio/Litro: ${precio:>10.2f}')
        print(f'Litros:       {litros:>10.2f}')
        print(f'TOTAL:        ${total:>10.2f}')
        print('--------------------------------------')

    # SIMULACION DE RENDIMIENTO
    elif op == 2:

        print('\n--- SIMULACION DE RENDIMIENTO ---')

        km_inicial = int(input('Kilometraje inicial: '))
        rendimiento = float(input('Rendimiento (km por litro): '))
        meses = int(input('Numero de meses: '))

        if km_inicial < 0 or rendimiento <= 0 or meses <= 0:
            print('\nError: los valores deben ser validos y positivos.')
            continue

        print('\n-----------------------------------------------')
        print(f'{"Mes":<8}{"Kilometraje":<15}{"Litros estimados"}')
        print('-----------------------------------------------')

        for mes in range(1, meses + 1):#ciclo for para calcular mes a mes

            km_recorridos = mes * 100
            kilometraje = km_inicial + km_recorridos

            litros = km_recorridos / rendimiento

            # Uso de // para obtener los kilometros completos
            km_completos = km_recorridos // 1

            # Uso de % para obtener el residuo de kilometros
            residuo = km_recorridos % 10

            # Uso de ** para proyectar el factor de crecimiento
            factor = 1 + (0.01 ** 1)

            consumo = litros * factor

            print(f'{mes:<8}{kilometraje:<15}{consumo:>8.2f} L')

        print('-----------------------------------------------')

    # CLASIFICADOR DE CLIENTE
    elif op == 3:

        print('\n--- CLASIFICADOR DE CLIENTE ---')

        litros_mes = float(input('Volumen de compra mensual (litros): '))

        if litros_mes <= 0:
            print('\nError: el volumen debe ser positivo.')
            continue

        if litros_mes < 100:
            cliente = 'Regular'
        elif litros_mes >= 100 and litros_mes <= 500:
            cliente = 'Premium'
        else:
            cliente = 'Flotilla'

        print('\n--------------------------------------')
        print(f'Volumen mensual: {litros_mes:.2f} L')
        print(f'Categoria:       {cliente}')
        print('--------------------------------------')

    # SALIR
    elif op == 4:

        print('\nPrograma terminado.')
        break#terminar ejecucion

    # OPCION INCORRECTA
    else:

        print('\nOpcion no valida.')
        continue
        #saltar al inicio del programa
    input('\nPresiona ENTER para continuar...')