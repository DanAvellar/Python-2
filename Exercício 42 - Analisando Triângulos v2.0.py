#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
seg1=float(input('Informe o primeiro segmento: '))
seg2=float(input('Informe o segundo segmento: '))
seg3=float(input('Informe o terceiro segmento: '))
soma=seg1+seg2
soma2=seg2+seg3
soma3=seg1+seg3
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1:
    print('É possível formar um triângulo com essas medidas.')
    if seg1 == seg2 and seg2 == seg3:
         print('É um triângulo EQUILÁTERO.')
    elif seg1 != seg2 and seg1 != seg3 and seg3 != seg2:
         print('É um triângulo ESCALENO.')
    else:
         print('É um triângulo ISÓSCELES.')
else:
    print('Não é possivel formar um triângulo com essas medidas.')
#Não é possível construir um triângulo se a soma da medida de dois segmentos for igual à medida de um terceiro segmento.