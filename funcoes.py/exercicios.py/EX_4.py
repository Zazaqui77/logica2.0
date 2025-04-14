import os 

os.system("cls || clear")

# Função para calcular a média
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

# Função para verificar a situação do aluno
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Função principal
def main():
    # Recebe as duas notas do aluno
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Calcula a média
    media = calcular_media(nota1, nota2)
    
    # Exibe a média
    print(f"A média do aluno é: {media:.2f}")
    
    # Verifica a situação do aluno
    situacao = verificar_situacao(media)
    print(f"O aluno está {situacao}.")

# Chama a função principal
if __name__ == "__main__":
    main()
