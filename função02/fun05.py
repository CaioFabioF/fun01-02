def nota(*n,sit=False):
    """
    -> Função de Notas
    :param n: As notas
    :param sit: Mostra a situação do aluno (Reprovado/Aprovado)
    :return ficha: Retorna os valores em um dicionário
    Função criada por Caio Fábio Felisberto
    """
    s = 0
    lista = []
    for b in n:
        s += b
        lista.append(b)
    q = len(lista)
    maior = max(lista)
    menor = min(lista)
    media = s / q
    ficha = {'Total': q, 'Maior': maior, 'Menor': menor, 'Média':media}
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