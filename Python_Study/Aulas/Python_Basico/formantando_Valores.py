"""
:s - Texto (strings)
:d - Inteiros (Int)
:f - Númeors de ponto flutuante (float)
:.(numero)f - Quantidade de casas decimais (float)
:(caractere) (> ou < ou ^) (Quantidade) (Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - centro
"""

num1 = 1
print(f'{num1:0>10}')
num2 = 115
print(f'{num2:0^10}')
num3 = 1921
print(f'{num3:0<10}')
num4 =132
print(f'{num4}')

nome = "Otavio Miranda"
nome_formatado = "{n:0<20}".format(n = nome)
print(nome_formatado)
print(f"{nome:#^50}")
