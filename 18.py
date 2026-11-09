# EXERCÍCIO 18: Inventário Infinito
# Enunciado: Crie um loop while que permita ao jogador adicionar itens a uma lista de inventário até que ele digite "sair".

inventario = []
item = ""
while item != "sair":
    item = input("Digite um item para adicionar (digite sair para parar): ")
    if item != "sair":
        inventario.append(item)
        print(f"{item} adicionado ao inventário!")
print("Inventário final:", inventario)
