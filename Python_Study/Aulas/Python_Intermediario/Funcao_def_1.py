"""
Funções - def(Parte 1)
"""
# def saudacao(msg='Ola', nome='Usuario'):
#   nome = nome.replace('e', '3')
#   msg = msg.replace('e', '3')
#   return f'{msg} {nome}'
# variavel = saudacao()
# print(variavel)

def divisao(n1, n2):
   if n2 == 0:
      return

   return n1 / n2

divide = divisao(8,4)

if divide:
   print(divide)
else:
   print('Conta Invalida')