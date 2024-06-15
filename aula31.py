"""
flag - marcar um local
none = nao valor
is e is not = é ou nao é (tipo, valor, identidade)
id = identidade
"""
# v1 = 'a'
# v2 = 'a'
# v3 = 'b'
# print(id(v1))
# print(id(v2))
# print(id(v3))

condicao = True
passou_no_if = None
if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
    