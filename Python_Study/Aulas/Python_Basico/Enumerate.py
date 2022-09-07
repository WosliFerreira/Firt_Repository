"""
Enumerate - Enumerar elementos da lista
"""
lista = [
    ['edu', 'Joao', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu']
]

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    print(minha_lista)
