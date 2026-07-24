import math

l1 = float(input('Qual o valor do cateto oposto: '))
l2 = float(input('Qual o valor do cateto adjacente: '))

#hipo = (l1 ** 2 + l2 ** 2) ** (1/2)
#print (" A medida da hipotenusa é {}".format(hipo))

hi = math.hypot(l1, l2)
print ('A medida da hipotenusa é {}'.format(hi))