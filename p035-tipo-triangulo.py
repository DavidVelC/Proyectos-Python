#-p035-tipo-triangulo.py
#Clasificar un triángulo según la longitud de sus tres lados.

print("Clasifica triangulos")
print('-'*50)
print("Ingresa la longitud de los tres lados de un triángulo.")

lado_a = float(input("Ingresa la longitud del lado A: "))
lado_b = float(input("Ingresa la longitud del lado B: "))
lado_c = float(input("Ingresa la longitud del lado C: "))

if lado_a == lado_b and lado_b == lado_c:
    print(f"Triángulo EQUILÁTERO (todos los lados son iguales).")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print(f"Triángulo ISÓSCELES (al menos dos lados son iguales).")
else:
    print(f"Triángulo ESCALENO (ningún lado es igual).")
print('FINISH')    
