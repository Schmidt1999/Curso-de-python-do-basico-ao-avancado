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

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1


if velocidade_carro_passou_radar_1:
    print('Voce passou da velocidade do radar')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print("O carro foi multado em radar 1")