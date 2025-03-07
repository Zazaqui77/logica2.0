import os

os.system("claear") 

#Solicitando Dados
print("""
================DIA===============    
1   \tSEGUNDA     
3   \tTERÇA
4   \tQUARTA 
5   \tQUINTA   
6   \tSEXTA
7   \tSÀBADO   
""")

dia= int(input("Digiteum número para o dia da semana: "))

#Verificando 
match dia:
    case 1 | 7: 
        resultado = "Fim de semana."
    case 2| 3 | 4 | 5 | 6:
        resultado = "Dia útil."
    case _:
        resultado = "Opção inválida"

#Exibindo resultados:
print()
print(f"Resultado:{resultado}")