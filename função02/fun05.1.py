def nota(*n,sit=False):
    """
    -> Função de Notas
    :param n: As notas
    :param sit: Mostra a situação do aluno (Reprovado/Aprovado)
    :return ficha: Retorna os valores em um dicionário
    Função criada por Caio Fábio Felisberto
    """
    media = sum(n) / len(n)
    ficha = {'Total': len(n), 'Maior': max(n), 'Menor': min(n), 'Média':media}
    if sit == True:
        if media < 60 :
            ficha['Situação'] = 'Reprovado'
        else: 
            ficha['Situação'] = 'Aprovado'
    return ficha
a = nota(10,24,52,64,32,sit=True)
j = nota(10,8,7,9,5)
print(a)
print(j)
help(nota)