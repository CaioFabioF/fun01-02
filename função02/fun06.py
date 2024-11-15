def ajuda(a):
    print(f'\033[1;37;44mAcessando o manual do comando {a}\033[1;37;44m')
    print(f'\033[1;30;45m{help(a)}\033[1;30;45m')
while True :
    print('\033[1;36;41mSistema de Ajuda PyHelp\033[1;36;41m')
    a = str(input('Função ou Biblioteca > '))
    if a == 'Fim':
        break
    ajuda(a)