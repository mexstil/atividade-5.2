# EXERCÍCIO 11: Soma Acumulada
# Enunciado: Crie um script que use um loop para somar todos os números de 1 a 5 e mostre o resultado final (1+2+3+4+5).

soma = 0
for valor in range(1, 6):
    soma = soma + valor
print(f"A soma de 1 a 5 é: {soma}")
