cid = (str(input('Em que cidade você nasceu: '))).strip()

if cid[0:5].upper() == 'SANTO' or cid[:3].upper() == 'SAO':
   print('Sua cidade começa com Santo ou São')
else:
   print('Sua cidade não começa com Santo ou São')
