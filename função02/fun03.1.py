def ficha(n='Desconhecido',g=0):
    if n.strip() =='' :
        n = '<Desconhecido>'
    else :
        n = str(n)
    if g.isnumeric() :
        g = int(g)
    else:
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato')
n = str(input('Digite o nome do seu jogador: '))
g = str(input('Digite a quantidade de gols no campeonato: '))
print(ficha(n,g))