#-p011-operadores-asignacion.py
#Ejemplifica el uso de operadores de asignacion

print("\033[2J\033\[H", end="")
print('0peradores de asignacion en pthon')

print("=" * 40)
x = 10
print(f"Valor inicial de x: {x}")

#Aplicar operadores
x += 5
print(f"x += 5 → x = {x}") 
x -= 3
print(f"x -= 3 → x = {x}") 
x *= 2
print(f"x *= 2 → x = {x}")
x /= 4
print(f"x /= 4 → x = {x}") 
x %= 3
print(f"x %= 3 → x = {x}") 
x **= 2
print(f"x **= 2 → x = {x}") 
x //= 2