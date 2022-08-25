"""
While - aula 7
Utilizado para realizar ações enquanto uma condição for verdadeira
"""
while True:
    print()
    num_1 = input('Digite um numero: ')
    operador = input('Digite um operador: ')
    num_2 = input('Digite outro numero: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Voce precisa digitar um numero.")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)
    # + - / *
    if  operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print("##Operador Invalido!##")