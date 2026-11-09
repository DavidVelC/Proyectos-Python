#p150-factorial.py
def factorial(num: int) -> int:
    res = 1
    for i in range(2, num + 1):
        res *= i
    return res
def main() -> None:
    numero = int(input("Introduce un número entero para calcular su factorial: "))
    if numero < 0:
        print("El factorial no está definido para números negativos.")
        return
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")
if __name__ == "__main__":
    main()