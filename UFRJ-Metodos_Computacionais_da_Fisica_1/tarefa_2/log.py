"""
 Função onde é dado o número x e n, calcula o logaritimo de x com uma precisão
de n termos na série.
"""
def log(x,n):
    soma=0
    for i in range(1,n+1): # i vai assumir todos os valores que estão na minha lista de 1 á n (n+1=5 termos).
        soma += 1/(2*i-1)*((x-1)/(x+1))**(2*i-1) #Atualiza o valor da soma para cada termo.
    print(f"O Ln de {x} é {round(2*soma,3)}.")
    return round(2*soma,3)
"""
  Quando utilizamos o módulo math para calcular Ln(1.2) com a função math.log(1.2),
 obtemos como resposta 0.1823215567939546 que é muito próximo ao obtido na função
 mesmo para 5 termos que nos da como resultado 0.1823215566990689, e com 3 termos
 nos da como resultado 0.18231905835211615.
"""
