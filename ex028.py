import random
print('Em qual numero eu estou pensando?')
print('--'*15)

escolhausuario = int(input('Escolha um numero de 1 a 5: '))

print("Voce escolheu o numero {}.".format(escolhausuario))


num =  [1, 2, 3, 4, 5]
escolhamaquina = random.choice(num)

print('Eu escolhi o numero {}.'.format(escolhamaquina))

if escolhausuario <= 5 and escolhausuario == escolhamaquina:
    print('Voce acertou')
elif escolhausuario > 5 or escolhausuario < 1:
    print('Numero digitado ivalido')
else:
    print('Voce errou')

