num=int(input('Informe um número inteiro>> '))
print('''Escolha uma das bases para conversão
[ 1 ] PARA CONVERTER PARA BINÁRIO, DIGITE 1
[ 2 ] PARA CONVERTER PARA OCTAL, DIGITE 2
[ 3 ] PARA CONVERTER PARA HEXADECIMAL, DIGITE 3''')
base=int(input('Informe a base da conversão>> '))
if base==1:
    print(f'O número {num}, convertido para Binário é:{bin(num)}')
elif base==2:
    print(f'O número {num}, convertido para Octal é: {oct(num)}')
else:
    print(f'O número {num}, convertido para Hexadecimal é: {hex(num)}')
