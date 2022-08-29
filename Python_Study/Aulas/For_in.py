"""
For in
Iterando strings com for
função range (start=0, stop, step=1)
"""
text = 'Python'
nova_string = ''

for letra in text:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)