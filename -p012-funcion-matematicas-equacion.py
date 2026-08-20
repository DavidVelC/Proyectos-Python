# -p012-funcion-matematicas-equacion.py 
x = 2
y = 2

fx_y_star = 3 * x**2 + mt.sqrt(x**2 + y**2) + mt.exp(mt.log(x))

fx_y_pow = 3 * mt.pow(x, 2) + mt.sqrt(mt.pow(x, 2) + mt.pow(y, 2)) + mt.exp(mt.log(x))

print(f"Resultado con el operador ** : {fx_y_star}")
print(f"Resultado con la función pow() : {fx_y_pow}")