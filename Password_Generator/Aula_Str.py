nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
ano_atual = 2022
nasc = ano_atual - idade
imc = peso / (altura ** 2)
print(f"{nome}, nascido em {nasc} voce possui {idade} anos de idade,voce tem {altura} de altura e peso de {peso}, tendo o imc corporal de {imc:.2f}  ")

