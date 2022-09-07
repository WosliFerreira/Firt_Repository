"""
Funções - def(Parte 1)
"""

def saudacao(msg='ola',nome='usuario'):
   nome = nome.replace('e', '3')
   msg = msg.replace('e', '3')
   return f'{msg} {nome}'

variavel = saudacao()

print(variavel)