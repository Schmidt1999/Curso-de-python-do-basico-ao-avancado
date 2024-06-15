"""
--- Introdução ao try/except ---
try -> tentar executar o código
except -> ocorreu algum erro ao executar
"""

numero_str = input('vou dobrar o numero que voce digitar: ')

try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_float} é {numero_float * 2:.1f}')
except:
    print("Isso não é um digito")



# if numero_str.isdigit():
#     
#  else:
#     



