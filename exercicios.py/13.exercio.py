# 1 - Limpando o terminal.
import os
os.system("clear")

# 2 - Solicitando dados para o usuário.
valor_produto = float(input("Digite o valor do produto: "))

print("""
==================== FORMA DE PAGAMETNO ====================
1   \tÁ vista
2   \tÁ prazo
""")
forma_de_pagamento = int(input("Digite a forma de pagamento: "))

# 3 - Verificando.
match forma_de_pagamento:
    case 1: 
        # Obtendo o valor do desconto de 10%.
        desconto = valor_produto * 0.10
        valor_com_desconto = valor_produto - desconto

        # Exibindo resultados.
        print(f"\nValor do produto: R$ {valor_produto}")
        print(f"Forma de pagamento: à vista")
        print(f"Valor do desconto: R${desconto}")
        print(f"Total a pagar: R$ {valor_com_desconto}")

    case 2: 
        quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
        if quantidade_parcelas >= 1 and quantidade_parcelas <= 6:
            valor_da_parcela = valor_produto / quantidade_parcelas
        
            # Exibindo resultados.
            print(f"\nValor do produto: R$ {valor_produto}")
            print(f"Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {quantidade_parcelas}")
            print(f"Valor por parcela: R$ {valor_da_parcela:.2f}")
            print(f"Total à prazo: R$ {valor_produto}")
        else:
            print("Opção inválida.")

    case _:
        print("Opção inválida.")