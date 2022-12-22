casa= float(input('Informe o valor da casa>> ')) #Variável que informa o valor da casa
salario= float(input('Informe o valor do salário>> ')) #Variável que informa o valor do sálario
anos = int(input('Informe os anos de financiamento>> ')) #Variável que informa os anos de financiamento
prestacao = casa /  (anos *12) #prestação vai ser igual a casa dividido pelos anos, vezes 12 para transformar em anos.
minimo = salario * 30/100 #minimo é onde vai realizar a conversão, a porcentagem em 30%
if prestacao>=minimo:
    print('Empréstimo negado!!!')
else:
    print('Empréstimo aprovado!!!')
