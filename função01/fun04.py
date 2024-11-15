def maior(valores):
    print('-='*70)
    print(f'Analisando os valores passados...')
    for a in valores:
        print(f'{a}',end=' ')
    print(f'Foram lidos ao todo {len(valores)} valores.')
    print(f'O maior valor foi {max(valores)}')
    print('-='*70)
valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
maior(valores)
