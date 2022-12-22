#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

n = 1
n = int(input('Digite um número para calcular o seu fatorial:'))
fat = n*(n-1)
for c in range(5,1,-1):
    print(f'result {c}')
    
---------------------------------------------------------

#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! ',end='')
while c > 0:
    print(c, end=' ')
    print('x' if c > 1  else f' = ',end=' ')
    f*= c
    c-= 1
print(f'O fatorial de {n} é {f}.')
