#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
escolha=int(input('''
JOGO DO JOKENPÔ
[0] PEDRA
[1] PAPEL
[2] TESOURA
Escolha suas opções:'''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
maquina=random.randint(0,2)
if escolha == 0 and maquina == 0:
    print('Empatado!')
elif escolha == 0 and maquina == 1:
    print('Você escolheu PEDRA e a máquina escolheu PAPEL, a máquina venceu!')
elif escolha == 0 and maquina == 2:
    print('Você escolheu PEDRA e a máquina escolheu TESOURA, você venceu!')
elif escolha == 1 and maquina == 0:
    print('Você escolheu PAPEL e a máquina escolheu PEDRA, você venceu!')
elif escolha == 1 and maquina == 1:
    print('Empatado!')
elif escolha == 1 and maquina == 2:
    print('Você escolheu PAPEL e a máquina escolheu TESOURA, a máquina venceu!')
elif escolha == 2 and maquina == 0:
    print('Você escolheu TESOURA e a máquina escolheu PEDRA, a máquina venceu!')
elif escolha == 2 and maquina == 1:
    print('Você escolheu TESOURA e a máquina escolheu PAPEL, você venceu!')
elif escolha == 2 and maquina == 2:
    print('Empatado!')

