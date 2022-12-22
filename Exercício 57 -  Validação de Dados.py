'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

n = 1
n = str(input('Informe o sexo [M/F]: ')).upper()
while n != 'M' and n != 'F':
    n = str(input('Dados inválidos, digite novamente: ')).upper()
print(f'Sexo {n} adicionado com sucesso.')
