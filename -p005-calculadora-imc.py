# p005-calculadora-imc.py
# Calcular el IMC de una persona
print("Calculadora de Índice de Masa Corporal (IMC):\n")
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso/(altura**2)
print(f"Tu IMC es: {imc:.2f}")