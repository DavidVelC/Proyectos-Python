#-p020-numero-suerte.py

print("Solicita al usuario su año de nacimiento y has las operaciones split y suma")
year = input("Ingresa tu año de nacimiento (4 dígitos): ")

print("Dígitos:", ", ".join(year))

suma = 0
for digito in year:
    suma += int(digito)

print(f"La suma de los dígitos es: {suma}")