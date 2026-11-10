#p159-nombres.py
def capturar_nombres() -> list[str]:
    datos = []
    print("Introduce nombres (deja en blanco para terminar):")
    while True:
        nombre = input("Nombre: ")
        if nombre == "":
            break
        datos.append(nombre)
    return datos

def une_procesa(lista1: list[str], lista2: list[str]) -> list[str]:
    nombres_unidos = lista1 + lista2
    nombres_invertidos = nombres_unidos[::-1]
    nombres_mayusculas = []
    for nombre in nombres_invertidos:
        nombres_mayusculas.append(nombre.upper())
    return nombres_mayusculas

#principal
nombres1 = ["Ana", "Juan", "Pedro", "Luis", "Maria"]
nombres2 = capturar_nombres()
nombres_procesados = une_procesa(nombres1, nombres2)
print(f"Nombres procesados: {nombres_procesados} - fueron: {len(nombres_procesados)}")