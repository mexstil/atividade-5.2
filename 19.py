# EXERCÍCIO 19: Efeito de Partícula
# Enunciado: Em um motor de jogo, queremos criar 100 partículas de fogo. Escreva a estrutura de um loop que repetiria a função criar_particula() 100 vezes.

def criar_particula():
    print("Partícula de fogo criada")

for contador in range(100):
    criar_particula()
