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
    case 1 : 
        resultado = "Janeiro"
    case 2 :
        resultado = "Fevereiro."
    case 3 :
        resultado = "Março."
    case 4 :
        resultado = "Abril."
    case 5 :
        resultado = "Maio."
    case 6 :
        resultado = "Junho."
    case 7 :
        resultado = "julho."
    case 8 :
        resultado = "Agosto"
    case 9 :
        resultado = "Setembro"
    case 10 :
        resultado = "Outubro"
    case 11 :
        resultado = "Novembro"
    case 12 :
        resultado = "Dezembro"
    
    

