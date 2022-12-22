#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
#SAÍDA
#Primeiro termo: 0
#Razão: 2
#0 2 4 6 8 10 12 14 16 18 ACABOU

pt = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
decimo = pt + (10-1) * r
for c in range(pt,decimo+r,r):
   print(c,end=' ')
print('ACABOU!')

