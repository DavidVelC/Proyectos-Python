#-p062-conversion-temperaturas.py
#introduce un rango de tmperatura y muestra su conversion a F°
#-p061-suma-200.py
while True:
    print('\033[H\033[J')
    suma = 0
    cont = 0
    print('Conversor de temperatura')
    start = float(input('Introduce un valor inicial: '))  
    final = float(input('Introduce un valor final: '))
    while start<=final:
        celsius = start
        farenheit = (celsius * 9/5) + 32
        print(f'{celsius}°C = {farenheit} °F')    
        start+=1

    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break
print('finish')