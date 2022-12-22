#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

preco=float(input('Informe o preço do produto: '))
pagamento=int(input('''FORMA DE PAGAMENTO
[1] Á vista dinheiro/cheque: 10% de desconto.
[2] Á vista no cartão: 5% de desconto.
[3] Em até 2x no cartão:Preço Formal. 
[4] Em 3x ou mais no cartão: 20% de juros.
Qual a opção? '''))
dinheiro=(preco/100)*10
vistcartao=(preco/100)*5
juros=(preco/100)*20
if pagamento == 1:
    print(f'O valor ficou R${preco-dinheiro:.2f}')
elif pagamento == 2:
    print(f'O valor ficou R${preco-vistcartao:.2f}')
elif pagamento == 3:
    print(f'O valor ficou em 2 parcelas de R${preco/2:.2f}')
elif pagamento == 4:
    parcela=int(input(f'Quantas parcelas?'))
    print(f'O valor ficou em {parcela} parcelas de {(preco+juros)/parcela:.2f} com juros.')
    print(f'Sua compra de {preco:.2f} vai custar {preco+juros:.2f} no final.')
