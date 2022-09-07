"""
Desempacotamento de listas
"""

listas = ['Luiz', 'Joao', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9]

# n1, n2, n3, *outra_lista, ultimo_da_lista = listas
# *outra_lista, ultimo_da_lista, n1, n2, n3, = listas
n1, n2, *_ = listas
print(n1, n2)
