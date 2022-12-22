#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
#desconsiderando os espaços. Exemplos de palíndromos:
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
#Palíndromo é uma palavra que pode ser lida com o mesmo sentido de trás para frente.

frase=str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É um Palíndromo.')
else:
    print('Não é um palíndromo.')