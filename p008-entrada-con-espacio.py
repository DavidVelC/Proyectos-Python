#-p008-entrada-con-espacio.py


print("Ingresa 3 numeros separado por un espacio")

n1, n2, n3 = input().split()
n1, n2, n3 = [ int(n1), int(n2), int(n3) ]

print("Los numeros son:")
print(n1, n2, n3)
print(n3, n2, n1)