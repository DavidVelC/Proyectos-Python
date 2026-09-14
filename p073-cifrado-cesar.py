#-p073-cifrado-cesar.py
# Cifra un mensaje con desplazamientos (Cifrado de Cesar)

print('\033[2J\033[H', end='')
print('Cifrado de Cesar')

mo = input('Mensaje: ')
d = int(input('Desplazamiento: '))

ms = cn = ''

for c in mo:
    if c.isalpha():  # solo letras
        ca = ord(c)
        bd = ord('a') if c.islower() else ord('A')
        cn = bd + (ca - bd + d) % 26
        ms = ms + chr(cn)
    else:
        ms = ms + c

print('Mensaje cifrado: ' + ms)