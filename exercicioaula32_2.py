entrada = input('Que horas são? ')

try:
    hora = int(entrada)
    
    if hora <= 11:
       print(f'Bom dia, são {hora} hora(s)')
    elif hora > 11 and hora < 18:
        print(f'Boa tarde, sao {hora} horas(s)')
    elif hora >= 18 and hora <= 23:
        print(f'Boa noite23, sao {hora} horas(s)')

except:
    print("Por favor digite apenas números inteiro.")