import time
def contador(i,f,p):
    print('-='*50)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    time.sleep(2)
    if p < 0 :
        p *= -1
    if i < f :
        cont = i
        while cont <= f :
            print(f'{cont:.2f} ',end='')
            time.sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f :
            print(f'{cont:.2f} ',end='')
            time.sleep(0.5)
            cont -= p
    print('\nFim!')
    print('-='*50)
i = float(input('Digite um início: '))
f = float(input('Digite o final: '))
p = float(input('Digite o passo: '))
contador(i,f,p)