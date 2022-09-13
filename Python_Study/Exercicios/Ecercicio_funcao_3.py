"""
Crie uma função que receba 2 numeros. o primeiro é um valor e o segundo um percentual (ex. 10%).
Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.
"""
def soma(n1, n2):
    variavel = n1 * (n2 / 100)
    return n1 + variavel

resultado = soma(140, 10)
print(resultado)
