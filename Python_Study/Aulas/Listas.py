"""
Listas em Python
Fatiamento
Append(Adciona), Insert(Insere), pop(Elimina o ultimo item da lista), del(Deleta um item da lista), clear, extend, +
Min, Max
Range
"""
#        0     1    2    3    4     5     6    7    8
#lista = ['A', 'B', 'C', 'D', 'E', 10.5, True, 'F', 'G' ]
#print(lista[0:7:2])
#l1 = [1, 2, 3]
#l2 = [4, 5, 6]
#l2.append('B')
#l2.insert(0, "banana")
#print(l2)
#l2.pop()
#print(l2)
#l2 = list(range(0, 100))
#l2.insert(0, 'Banana')
#print(l2)
#del(l2[3:5])
#del(l2[0])
#print(l2)
#print(max(l2))
#print(min(l2))
#for valor in l2:
#    print(valor)

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu!!')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print("Isso nao vale, digite apenas uma letra.")
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} nao existe na palavra seecreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f"Voce Ganhou o Game!!, a palavra secreta era {secreto_temporario}")
        break
    else:
       print(f"A palavra secreta esta assim: {secreto_temporario}")

    if letra not in secreto:
        chances -= 1

    print(f'restam apenas {chances} chances.')


