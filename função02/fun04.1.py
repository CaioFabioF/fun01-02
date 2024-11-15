def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric() :
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok == True:
            break
    return valor
a = leiaInt('Digite um número: ')
print(f'Você digitou o número {a}')