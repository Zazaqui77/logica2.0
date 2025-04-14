import os

os.system("cls || clear")

menu = {
    1: ("Picanha", 25.00),
    2: ("Lasanha", 20.00),
    3: ("Strogonoff", 18.00),
    4: ("Bife Acebolado", 15.00),
    5: ("Pão com ovo", 5.00)
}


pedidos = []
valor_total = 0

while True:
    print("\nCardápio:")
    for codigo, (prato, valor) in menu.items():
        print(f"{codigo} - {prato}: R$ {valor:.2f}")
    
    escolha = int(input("Digite o código do prato desejado: "))
    if escolha in menu:
        prato, valor = menu[escolha]
        pedidos.append((prato, valor))
        valor_total += valor
    else:
        print("Código inválido. Tente novamente.")
        continue
    
    continuar = input("Deseja escolher outro prato? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nResumo do pedido:")
for prato, valor in pedidos:
    print(f"{prato}: R$ {valor:.2f}")

print(f"Valor total: R$ {valor_total:.2f}")

gorjeta = input("Deseja pagar 10% de gorjeta para o garçom? (s/n): ").strip().lower()
if gorjeta == 's':
    valor_gorjeta = valor_total * 0.10
    valor_total += valor_gorjeta
    print(f"Gorjeta: R$ {valor_gorjeta:.2f}")

print(f"Valor final a pagar: R$ {valor_total:.2f}")
