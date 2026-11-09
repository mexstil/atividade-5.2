# EXERCÍCIO 13: Números Pares
# Enunciado: Escreva um código que percorra o intervalo de 1 a 20 e imprima apenas os números que são pares.

for n in range(1, 21):
    if n % 2 == 0:
        print(n)
