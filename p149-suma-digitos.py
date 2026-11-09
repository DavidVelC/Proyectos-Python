#p149-suma-digitos.py
def suma_digitos(num: int) -> int:
    numero = abs(num)
    suma = 0
    while numero!=0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma
def main() -> None:
    numero = int(input("Introduce un número entero: "))
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es {resultado}")
if __name__ == "__main__":
    main()