import os

os.system("cls || clear")

#Solicitando dados para o usuario

def main():
    qtd_pares = 0
    qtd_impares = 0
    soma_pares = 0
    soma_total = 0
    total_numeros = 0
    
    while True:
        num = int(input("Digite um número (0 para sair): "))
        
        if num == 0:
            break
        
        total_numeros += 1
        soma_total += num

        if num % 2 == 0:
            qtd_pares += 1
            soma_pares += num
        else:
            qtd_impares += 1

    if qtd_pares > 0:
        media_pares = soma_pares / qtd_pares
    else:
        media_pares = 0

    if total_numeros > 0:
        media_geral = soma_total / total_numeros
    else:
        media_geral = 0

    print(f"Quantidade de números pares: {qtd_pares}")
    print(f"Quantidade de números ímpares: {qtd_impares}")
    print(f"Média dos valores pares: {media_pares:.2f}")
    print(f"Média geral dos números lidos: {media_geral:.2f}")

if __name__ == "__main__":
    main()
