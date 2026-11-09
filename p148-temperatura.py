#p148-temperatura.py
def celsius_a_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32
def fahrenheit_a_celsiuss(f: float) -> float:
    return (f - 32) * 5/9

def main() -> None:
    print('Conversión de temperaturas:')
    print('1. Celsius a Fahrenheit')
    print('2. Fahrenheit a Celsius')
    opcion = int(input('Elige una opción (1 o 2): '))
    if opcion == 1:
        print('Dame la temperatura en celsius:')
        c = float(input())
        f = celsius_a_fahrenheit(c)
        print(f'{c}°C son {f}°F')
    elif opcion == 2:
        print('Dame la temperatura en Fahrenheit:')
        f = float(input())
        c = fahrenheit_a_celsiuss(f)
        print(f'{f}°F son {c}°C')
    else:
        print('Opción inválida')

if __name__ == "__main__":
    main()