
entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = "impar"

    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Por favor digite um numero inteiro')