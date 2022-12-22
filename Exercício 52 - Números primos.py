#Faça um programa que leia um número inteiro
#e diga se ele é ou não um número primo.
#SAÍDA
#Digite um número
#12345678910
#O Número 10 foi divisível 4 vezes
#e por isso ele NÃO É PRIMO!

n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot +=1
    else:
        print('\033[31m', end=' ')
    print(c,end=' ')
print(f'\n O número {n} foi divisível {tot} vezes.')
if tot == 2:
    print(' Portanto, é um número primo.')
else:
    print(' Portanto, não é um número primo.')