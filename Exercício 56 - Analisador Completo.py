#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
#qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos.

tot_mulher=0
soma=0
maior=0
nomeHomemMais_Velho = ''

for c in range(1,5):
    nome = input(f'Informe o nome da {c}ª pessoa: ')
    idade = int(input(f'Informe a idade da {c}ª pessoa: '))
    sexo = input('Masculino ou Feminino? [M/F] ').upper()[0]
    soma = soma + idade
    if sexo in 'Ff' and idade < 20:
        tot_mulher  += 1
    if c == 1 and sexo in 'Mm':
         maior = idade
         nomeHomemMais_Velho = nome
    if sexo in 'Mm' and idade > maior:
         maior = idade
         nomeHomemMais_Velho = nome

print(f'A média de idade do grupo é de {soma/4} anos.')
print(f'O homem mais velho tem {maior} anos e se chama {nomeHomemMais_Velho}.')
print(f'Ao todo temos {tot_mulher} mulheres com menos de 20 anos.')
