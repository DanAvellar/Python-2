#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

soma=0
for c in range(1,7):
    c = int(input('Número inteiro: '))
    if c%2==0:
        soma = soma + c
    else:
        print('Desconsiderado, pois é ímpar.')
print(f'O resultado das soma dos pares é de {soma}.')