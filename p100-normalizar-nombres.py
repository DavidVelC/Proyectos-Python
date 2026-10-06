#p100-normalizar-nombres.py
#Pasa los nombres a mibnuscula y elimuina espaciocs
print('\033[H\033[J')
print("\033[1;32m" + 'Actividad 14 Normaliza nombres' + "\033[0m")

name = [" Juan ", " Maria ", " Pedro ", " Ana ", " Luis "]
normalized = [name.strip().lower() for name in name]

print('Nombres originaes: ', name)
print('Nombres normalizados: ', normalized)