num = int(input('Informe um número 0 e 9999: '))
#print (len(num))
#if len(num) == 4:
#    print('Unidade: {} '.format((num[3])))
#    print('Dezenas: {} '.format(num[2]))
#    print('Centenas: {} '.format(num[1]))
#    print('Milhar: {} '.format(num[0]))
#elif len(num) == 3:
#    print('Unidade: {} '.format((num[2])))
#    print('Dezenas: {} '.format(num[1]))
#    print('Centenas: {} '.format(num[0]))
#elif len(num) == 2:
#    print('Unidade: {} '.format((num[1])))
#    print('Dezenas: {} '.format((num[0])))
#elif len(num) == 1:
#    print('Unidade: {} '.format((num[0])))


u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))