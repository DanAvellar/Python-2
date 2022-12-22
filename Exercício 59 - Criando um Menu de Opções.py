#Crie um programa que leia dois valores e mostre um menu na tela:
'''[1] somar
   [2] multiplicar
   [3] maior
   [4] novos números
   [5] sair do programa'''
from time import sleep
menu = 0
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
while menu != 5 or menu > 5:
    menu = int(input('[1] Somar''\n[2] Multiplicar''\n[3] Maior' '\n[4] Novos números''\n[5] Sair do programa'
          '\nEscolha entre uma das opções:'))
    if menu == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}.')
    if menu == 2:
        print(f'A multiplicação entre {n1} x {n2} é {n1*n2}.')
    if menu == 3:
        if n1>n2:
            print(f'Entre {n1} e {n2}, o maior valor é {n1}.')
        if n2>n1:
            print(f'Entre {n1} e {n2}, o maior valor é {n2}.')
        if n1 == n2:
            print('Os números são iguais.')
    if menu == 4:
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    if menu == 5:
        print('Você decidiu sair do programa.')
    if menu > 5:
        print('Opção inválida, tente novamente:')
    sleep(1)
print('Finalizando...')

