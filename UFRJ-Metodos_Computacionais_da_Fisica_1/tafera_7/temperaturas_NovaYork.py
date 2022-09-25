"""
Nome: Estevão Soares;
DRE: 118045201
MCF1
"""
temperaturas_NovaYork_Celsius=[]
temperaturas_NovaYork_Fahrenheit=open("C:/Users/Matrix/Desktop/University/Matérias/periodo8/MCF1/Aula8/o_temperaturas_NovaYork_Fahrenheit.txt", 'r')
numero_interacoes=0
try:
    while True:
        line_Fahrenheit = temperaturas_NovaYork_Fahrenheit.readline()
        if line_Fahrenheit.split()[0]=="#":
            temperaturas_NovaYork_Celsius.append(line_Fahrenheit)
        if line_Fahrenheit.split()[0]!="#" and numero_interacoes<14: #Pois, segundo o arquivo txt, as contas de tranformações de Celsius para Fahrenheit devem ser feitas nesse range de números!Como o número de interações começa no 0, o 2 é o inicio da linha onde há conversão!
            temperaturas_NovaYork_Celsius.append(f"{line_Fahrenheit.split()[0]} {round((5*float(line_Fahrenheit.split()[1])-160)/9,2)}\n") # Pega a String com o mês e junta com uma separação de espaço com a temperatura em celsius.
        numero_interacoes+=1
        if not line_Fahrenheit:
            break
    temperaturas_NovaYork_Celsius_join = " ".join(temperaturas_NovaYork_Celsius)
    Criacao_Arquivo = open('temperaturas_NovaYork_Celsius.txt','w')
    Criacao_Arquivo.write(temperaturas_NovaYork_Celsius_join)
    Criacao_Arquivo.close()
except IndexError:
    print(f"Seu programa deu erro na {numero_interacoes} interação")
    exit