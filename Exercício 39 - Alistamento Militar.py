#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
anonasc=int(input('Ano de Nascimento: '))
sexo=int(input('Se for do Sexo Masculino, digite 1, '
               'caso seja do Sexo Feminino, digite 2: '))
tempo=(atual-anonasc)
tempofalta=(anonasc-2004)
tempopassou=(2004-anonasc)
if sexo == 2:
    print('Você não precisa se alistar, pois é do sexo Feminino.')
else:
    print('Você precisa se alistar, pois é do sexo Masculino.')
    if anonasc == 2004:
        print(f'Você nasceu em 2004 e tem {tempo} anos em 2022.')
        print('Esse é o ano da sua maioridade, é preciso se alistar IMEDIATAMENTE!!!')
    elif anonasc > 2004:
        print(f'Você nasceu em {anonasc} e tem {tempo} anos em 2022.')
        print(f'Faltam {tempofalta} anos para você realizar o seu ALISTAMENTO.')
        print(f'O seu alistamento será em {atual+tempofalta}')
    elif anonasc < 2004:
        print(f'Você nasceu em {anonasc} e tem {tempo} anos em 2022.')
        print(f'Você deveria ter se alistado a {tempopassou} anos.')
        print(f'O seu alistamento foi em {anonasc+18}.')
