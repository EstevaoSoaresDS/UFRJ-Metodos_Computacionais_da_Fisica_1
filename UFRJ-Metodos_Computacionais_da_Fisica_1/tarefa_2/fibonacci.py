'''
 O código imprime os 100 primeiro números da série de Fibonacci.
'''
def fibonacci():
    n_menos_1=1
    n_menos_2=0
    termo = 3
    série_fibonacci_100=[n_menos_2,n_menos_1,]
    while termo <= 100:
        termo_atual = n_menos_2 + n_menos_1 # Termo atual da série é igual a soma dos 2 anteriores.
        série_fibonacci_100.append(termo_atual) #adiciona na lista até o termo 100.
        n_menos_2 = n_menos_1
        n_menos_1 = termo_atual #Aqui atualizamos os valores para percorrer todos os 100 termos.
        termo +=1
    print(série_fibonacci_100)
