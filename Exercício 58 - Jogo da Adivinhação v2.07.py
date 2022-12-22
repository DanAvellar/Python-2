#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.


print('JOGO DA ADIVINHAÇÃO v2.07')
import random
n = 1
tot = 0
number = random.randint(1,10)
n = int(input('Informe um número de 1 até 10 : '))
while n != number:
    n = int(input('Esse não foi o número sorteado, tente novamente: '))
    tot+=1
print('Acertou o número sorteado')
print(f'Foram necessários {tot} palpites para acertar o número sorteado.')