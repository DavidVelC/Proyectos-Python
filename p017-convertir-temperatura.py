#-p017-convertir-temperatura.py
# temperatura de grados Celsius a grados Fahrenheit.

print('Temperatura de grados Celsius a grados Fahrenheit')
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

farenheit = (celsius * 9/5) + 32

print(f'Temperatura en farenheit es: {farenheit:.2f}')