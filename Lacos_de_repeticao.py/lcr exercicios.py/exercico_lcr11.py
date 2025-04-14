import os

os.system("cls || clear")

def exibir_menu():
    print("\nMenu de Pratos:")
    print("1 - Pizza - R$ 30.00")
    print("2 - Hambúrguer - R$ 20.00")
    print("3 - Sushi - R$ 50.00")
    print("4 - Salada - R$ 15.00")
    print("5 - Massa - R$ 25.00")
    print("6 - Churrasco - R$ 40.00")
    print("7 - Sobremesa - R$ 10.00")
    print("0 - Finalizar pedido")

def obter_preco(prato):
    precos = {
        1: ("Pizza", 30.00),
        2: ("Hambúrguer", 20.00),
        3: ("Sushi", 50.00),
        4: ("Salada", 15.00),
        5: ("Massa", 25.00),
        6: ("Churrasco", 40.00),
        7: ("Sobremesa", 10.00),
    }
    return precos.get(prato, (None, 0))

def main():
    pedido = []
    total = 0
    
    while True:
        exibir_menu()
        try:
            codigo = int(input("Digite o código do prato desejado: "))
            if codigo == 0:
                break
            nome_prato, preco = obter_preco(codigo)
            if nome_prato:
                pedido.append((codigo, nome_prato, preco))
                total += preco
                print(f"{nome_prato} adicionado ao pedido.")
            else:
                print("Código inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    
    if not pedido:
        print("Nenhum prato foi selecionado.")
        return
    
    print("\nFormas de pagamento:")
    print("1 - À vista (10% de desconto)")
    print("2 - Cartão de crédito (10% de acréscimo)")
    
    while True:
        try:
            opcao_pagamento = int(input("Escolha a forma de pagamento: "))
            if opcao_pagamento == 1:
                desconto = total * 0.10
                total_final = total - desconto
                forma_pagamento = "À vista"
                break
            elif opcao_pagamento == 2:
                acrescimo = total * 0.10
                total_final = total + acrescimo
                forma_pagamento = "Cartão de crédito"
                break
            else:
                print("Opção inválida. Escolha 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    
    print("\nResumo do Pedido:")
    for codigo, nome, preco in pedido:
        print(f"{codigo} - {nome} - R$ {preco:.2f}")
    print(f"Subtotal: R$ {total:.2f}")
    print(f"Forma de pagamento: {forma_pagamento}")
    print(f"Valor final a ser pago: R$ {total_final:.2f}")
    
if __name__ == "__main__":
    main()
