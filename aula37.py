"""
repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
contador = 0

while contador <= 1000:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue

    if contador >= 10 and contador < 20:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 400:
        break

print('Acabou')
