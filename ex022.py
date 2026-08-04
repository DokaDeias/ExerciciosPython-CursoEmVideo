nome = str(input('Digite o seu nome completo: ')).strip()

separate = nome.split()

print('Analisando seu nome...')
print('Seu nome é', nome)
print("Seu nome em maisuculo é", nome.upper())
print('Seu nome em minuscula é', nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print ('seu primeiro nome é {}'.format(separate[0]))

