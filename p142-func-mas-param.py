#p142-func-mas-param.py
def saluda(*todos: str) -> None:
    for nombre in todos:
        print(f"Bienvenido {nombre}, tu nombre tiene {len(nombre)} caracteres")

saluda("David", "Cynthia", "Carlos")

def edades(*edades:int) -> None:
    print(edades)
    for edad in edades:
        print(f"Edad: {edad} años")

edades(23, 22, 44)