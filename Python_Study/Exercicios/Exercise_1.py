# Faça um programa que peça ao usuario para digitar um numero inteiro, informe se este numero é par ou ímpar.
# Caso o usuario não digite um número inteiro, informe que não é um numero.

num_inteiro = input('Digite um numero:  ')
if not num_inteiro.isdigit():
    print('Isso não é um número inteiro.')
else:
    num_inteiro = int(num_inteiro)
    if num_inteiro % 2 == 0:
        print(f'{num_inteiro} é Par')
    else:
        print(f'{num_inteiro} é Ímpar')

