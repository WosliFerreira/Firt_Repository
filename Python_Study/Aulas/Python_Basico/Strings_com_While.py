#        Indices
#        0123456789.......................33
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
input_do_usuario = input('Qual a letra deseja colocar maiuscula? ')
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += frase[contador]
    contador += 1

print(nova_string)