"""
Operador Tenário
"""
# logged_user = False
# msg = 'Usuario logado!' if logged_user else 'Usuario precisa logar!'
repeticao = 0
while repeticao < 5:
    idade = input('Qual a sua idade: ')
    if not idade.isnumeric():
        print('Voce precisa digitar apenas numeros')
        continue
    else:
      idade = int(idade)
      e_de_maior = (idade >= 18)
      msg = 'Pode beber' if e_de_maior else 'Nao pode beber'
      print(msg)
      repeticao += 1
print("Fim")