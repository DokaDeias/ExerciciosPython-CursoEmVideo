nome = (str(input('Digite seu nome completo: '))).strip()

#print ('Seu nome tem Silva? {}'.format('Silva' in nome.upper))

if 'SILVA' in nome.upper():
   print('Seu nome tem Silva')
else:
   print('Seu nome não tem Silva')