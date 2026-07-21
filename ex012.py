preco = (float(input("Qual o preço do produto? R$")))

desc5 = preco * 0.05
desc10 = preco * 0.1
desc50 = preco * 0.5
desc75 = preco * 0.75

print("O seguinte produto no valor de {:.2f}, com o desconto aplicado de 5% sai a R${:.2f}".format(preco, preco - desc5))
print("O seguinte produto no valor de {:.2f}, com o desconto aplicado de 10% sai a R${:.2f}".format(preco, preco - desc10))
print("O seguinte produto no valor de {:.2f}, com o desconto aplicado de 50% sai a R${:.2f}".format(preco, preco - desc50))
print("O seguinte produto no valor de {:.2f}, com o desconto aplicado de 75% sai a R${:.2f}".format(preco, preco - desc75))