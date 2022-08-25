"""
Manipulando strings - Aula 6
* String indices
* Fatiamento de stings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""
# Positivos
texto = 'Python_s2'
# Negativos -[987654321]

url = 'www.google.com.br/'

print(url[:-1])

print(len(texto))
nova_string = texto[:6]
nova_string2 = texto[:-1]
nova_string3 = texto[:6:3]

print(nova_string)
print(nova_string2)
print(nova_string3)


for letra in texto:
    print(letra)