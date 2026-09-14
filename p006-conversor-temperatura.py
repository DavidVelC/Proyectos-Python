#-p006-conversor-temperatura.py
#Celsius a farenheit
print("Conversor de Temperatura (Celsius a Fahrenheit):\n")

celsius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"Temperatura en Fahrenheit es: {fahrenheit:.2f}°F")