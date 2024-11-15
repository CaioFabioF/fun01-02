def leiaInt(n):
        a = n.isnumeric()
        if a == False :
            print('Erro! Digite um número')
        if a == True:
            print(f'{n} é um número')
while True:
    b = str(input('Digite um número: '))
    leiaInt(b)
    if b.isnumeric() == True:
         break
 