import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]
escolha = random.choice(lista)

print('O aluno escolhido para limpar a lousa foi {}'.format(escolha))

#import random
#print('-'*20)
#print ('Quem vai apagar a lousa?')
#print('-'*20)
#print('   Sorteando...')
#print('-'*20)
#aluno = random.randint(1, 4)

#if aluno == 1:
#    print("Emicida vai apagar a lousa")
#elif aluno == 2:
#    print("Jotape vai apagar a lousa")
#elif aluno == 3:
#    print('Rashid vai apagar a lousa')
#elif aluno == 4:
#   print("Projota vai apagar a lousa")
