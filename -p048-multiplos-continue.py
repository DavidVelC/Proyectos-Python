#-p048-multiplos-continue.py
print('\033[2J\033[H', end='')
print('Imprime multiplos de 10 del 1 a 200')
c=0
while c<=200:
    c+=1
    if c%10!=0: continue
    print(f'{c} ')
print('FINISH')