# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

tot1=0
tot2=0
from datetime import date
data_atual=date.today().year
for pessoa in range(1,8):
    ano = int(input(f'Em que ano a {pessoa}ª pessoa nasceu?' ))
    nasc = data_atual-ano
    if nasc >=18:
        tot1+=1
    else:
        tot2+=1
print(f'Ao todo tivemos {tot1} pessoas maiores de idade.')
print(f'E também tivemos {tot2} pessoas menores de idade.')
