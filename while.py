#Estrutura de repetição com teste lógico = O While serve para quando não sabemos determinado valor.
#Exemplo: Leia a idade de todas as pessoas que vierem no balcão, porém, não há a informação do número de pessoas que virão.
#n = 1
#while n != 0:
#n = int(input('Digite um valor: '))
#print('Fim')

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')


