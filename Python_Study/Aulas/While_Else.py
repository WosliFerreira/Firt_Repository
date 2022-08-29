"""
While / Else - Aula 8
Contadores
Acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')
print('Isso será executado')