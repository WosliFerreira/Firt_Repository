# Faça um programa que pergunte a hora ao usuario e baseando no horario decrito, exiba a saudação apropriada.
# Ex: bom dia 0 -11, boa tarde 12 - 17, boa noite 18-23

horario = input("Digite um Horario(0-23): ")

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print("Horario deve estar entre 0 e 23")
    else:
        if horario <= 11:
            print("Bom dia!")
        elif horario <= 17:
            print("Boa Tarde!")
        else:
            print("Boa Noite!")
else:
    print("Por favor, digite um horario entre 0 e 23")
