import datetime
def voto(ano):
    anoa = 2024
    valor = anoa - ano
    if valor < 16 :
        return f'Com {valor} anos, o voto é Negado.'
    elif 16 <= valor < 18 or valor > 65 :
        return f'Com {valor} anos, o voto é Opcional'
    else:
        return f'Com {valor} anos, o voto é Obrigatório'
a = int(input('Digite o ano em que você nasceu: ')) 
print(voto(a))