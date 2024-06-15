"""
repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
contador = 0

while contador <= 1000000:
    contador += 1
    print(contador)

    if contador == 400:
        break

print('Acabou')