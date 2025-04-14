import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")

def main():
    dados = []
    
    while True:
        limpar_tela()
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            while True:
                try:
                    idade = int(input("Idade: "))
                    sexo = input("Sexo (M/F): ").strip().upper()
                    salario = float(input("Salário: "))

                    if sexo not in ["M", "F"]:
                        print("Sexo inválido! Digite M ou F.")
                        continue

                    dados.append({"idade": idade, "sexo": sexo, "salario": salario})

                    continuar = input("Adicionar outra pessoa? (S/N): ").strip().upper()
                    if continuar != "S":
                        break
                except ValueError:
                    print("Entrada inválida! Tente novamente.")
                    
        elif opcao == "2":
            limpar_tela()
            if not dados:
                print("Nenhum dado cadastrado!")
            else:
                media_salario = sum(p["salario"] for p in dados) / len(dados)
                idades = [p["idade"] for p in dados]
                maior_idade = max(idades)
                menor_idade = min(idades)
                mulheres_acima_5000 = sum(1 for p in dados if p["sexo"] == "F" and p["salario"] >= 5000)

                print(f"Média de salário do grupo: R$ {media_salario:.2f}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {mulheres_acima_5000}")
            
            input("\nPressione Enter para voltar ao menu...")
        
        elif opcao == "3":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

