# EXERCÍCIO 20: Verificação de Vencedor
# Enunciado: Imagine uma corrida com 5 ciclistas. Use um loop para ler o tempo de cada um e identificar quem teve o menor tempo.

menor_tempo = 9999
vencedor = 0

for ciclista in range(1, 6):
    tempo = float(input(f"Digite o tempo do ciclista {ciclista}: "))
    if tempo < menor_tempo:
        menor_tempo = tempo
        vencedor = ciclista

print(f"O ciclista {vencedor} é o vencedor com tempo de {menor_tempo}")
