def fazer_pedido(cardapio):
    pedido = [] # colchetes vazio inicia uma lista vazia "[]"
    
    while True:
        sabor = input("Digite o sabor da pizza que deseja ou 'SAIR' para finalizar: ")
        if sabor == "sair":
            break
        elif sabor in cardapio:
            pedido.append(sabor)
            print(f'🍕 {sabor} adicionada no seu pedido!.')
        else:
            print(f'Esse sabor não está disponível 😥. Escolha outro sabor! ')
    return pedido

cardapio = ["Mussarela", "Calabresa", "Pepperoni", "Frango com catupiry"]
pedido_cliente = fazer_pedido(cardapio)
print(pedido_cliente) 