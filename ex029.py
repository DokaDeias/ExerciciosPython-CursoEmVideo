print('Calculador de multa')
print('--'*15)
km = float(input('Qual a velocidade do carro? '))

multa = (km - 80) * 7


if km > 80:
    print('Você ultrapassou o limite de velocidade e será multado')
    print('--' * 15)
    print('Calculando multa')
    print('Você irá pagar R${:.2f}'.format(multa))
else:
    print('--' * 15)
    print("Parabéns! \nVocê esta dentro do  limite de velocidade")