import random
numeros = []
def sorteia():
    print('-='*70)
    for c in range(0,10):
        numeros.append(random.randint(0,10))
    print(f'Os valores são:')
    for a in numeros:
        print(f'{a}',end=' ')
def somapar():
    s = 0
    for a in numeros:
        if a % 2 == 0:
            s += a
    print(f'\nA soma dos valores pares foi {s}')
    print('-='*70)
sorteia()
somapar()