#p140-func-param-nombre.py
def saluda(apaterno: str, amaterno: str, nombre: str) -> None:
    print(f'Hola {nombre} {apaterno} {amaterno}, bienvenido')

saluda('Velázquez', 'Calvillo', 'David')
saluda(nombre='Ana', amaterno='Martinez', apaterno='Lopez')