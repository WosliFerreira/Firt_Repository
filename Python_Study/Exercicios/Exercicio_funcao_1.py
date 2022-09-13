"""
Crie uma função que exibe uma saudação com os paramentos saudação e nome
"""

def saudacao(msg='bom dia', user='Jovem'):
    return f'{msg} {user}'


variavel = saudacao()
print(variavel)
