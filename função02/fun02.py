def fatorial(n,show=False) :
    """
    -> Função de Fatorial
    :param n: O número a ser mostrado o fatorial
    :param show: Mostra o processo da fatoração
    :return f: Retorna o fatorial do número n
    Função criada por Caio Fábio Felisberto
    """
    f = 1
    for c in range(n,0,-1) :
        if show == True :
            print(f'{c}',end='')
            if c > 1 :
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f
print(fatorial(7,show=True))
help(fatorial)