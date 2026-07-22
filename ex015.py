carro = input('Qual carro Foi alugado? ')
D = int(input('Quantos dias o carro foi alugado? '))
Km = float(input('Quantos Km rodados? '))


total = D * 60 + Km * 0.15

taxa = 500

print('-' * 25)
print("CALCULANDO VALORES PARA{}".format(carro))
print('-' * 25)
print("Taxa de aluguel: R${:.2f}".format(taxa))
print('-' * 25)
print("Dias = {}".format(D))
print("valor = R${:.2f}".format(D*60))
print('-' * 25)
print("Quilometros Rodados = {}".format(Km))
print("Valor = R${:.2f}".format(Km*00.15))
print('-' * 25)
print("Total a pagar = R${:.2f}".format(total+taxa))
print('-' * 25)
print('OBRIGADO POR ALUGAR SEU CARRO')
print('NA FUNILARIA ZECA URUBU')
print('-' * 25)