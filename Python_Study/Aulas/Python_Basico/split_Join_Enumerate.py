"""
Split - Divide uma string
Join - Junta uma lista
Enumerate - Enumera elementos da lista
"""

string = 'O Brasil é o pais do futebol,o Brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')
#print(lista1)
#print (lista2)
palavra = ''
contagem = 0
for valor in lista1:
   qtd_vezes  = lista1.count(valor)

   if qtd_vezes > contagem:
       contagem = qtd_vezes
       palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem})x')