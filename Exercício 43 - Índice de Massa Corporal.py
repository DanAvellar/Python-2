# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
weight = float(input('Weight: '))
height = float(input('Height: '))
imc = weight/(height*height)
if imc <18.5:
    print(f'O seu IMC é de {imc:.1f} e você está ABAIXO DO PESO.')
elif imc >= 18.5 and imc <=25:
    print(f'O seu iMC é de {imc:.1f} e você está no PESO IDEAL.')
elif imc >= 25 and imc <=30:
    print(f'O seu IMC é de {imc:.1f} e você está com SOBREPRESO.')
elif imc >= 30 and imc <=40:
    print(f'O seu IMC é de {imc:.1f} e você possui OBESIDADE.')
else:
    print(f'O seu IMC é de {imc:.1f} e você possui OBESIDADE MÓRBIDA.')