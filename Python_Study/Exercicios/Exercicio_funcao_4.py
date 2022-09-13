"""
Se o parametro da funçao for divisivel por 2, retornee fizz, se o paramentro da função for divisivel por 5,retorne buzz.
Se o paramentro da função for divisivel por 5 e 3 retorne, FizzBuzz, caso contrario retorne numero Enviado.
"""


def funcao(n1):
    if n1 % 2 == 0:
        return "Fizz"
    elif n1 % 5 == 0:
        return 'Buzz'
    elif n1 % 3 == 0 and n1 % 5 == 0:
        return "FizzBuzz"
    else:
        return "Numero Enviado"


resultado = funcao(9)
print(resultado)
