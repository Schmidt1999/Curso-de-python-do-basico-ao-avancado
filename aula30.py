"""
CONSTANTE = variáveis que não vão mudar 
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim) 
"""

velocidade = 61 # velocidade atual do carro
local_carro = 99 #local em que o carro está na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega

if velocidade > RADAR_1:
    print('Voce passou da velocidade do radar')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print("O carro foi multado em radar 1")