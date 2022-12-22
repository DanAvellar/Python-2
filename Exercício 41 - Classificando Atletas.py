#A Confederação Nacional de Natação precisa de um programa que leia o ano de
#nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
anonasc=int(input('Ano de nascimento: '))
data=atual-anonasc
print(f'O Atleta tem {data} anos.')
if data <= 9:
    print('A sua classificação é MIRIM.')
elif data <= 14:
    print('A sua classificação é INFANTIL.')
elif data <=19:
    print('A sua classificação é JÚNIOR.')
elif data <=25:
    print('A sua classificação é SÊNIOR.')
else:
    print(f'A sua classificação é MASTER.')
