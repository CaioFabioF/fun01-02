def dicotomia(lst):
    pos = 0    
    while pos < len(lst) :
        lst[pos] *= 2
        pos += 1
valores = []
for c in range(0,5):
    valores.append(int(input('Digite um número para ser dobrado: ')))
dicotomia(valores)
print(valores)