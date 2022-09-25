'''
 Código que imprime uma tabela de 12 conversões de graus Celsius para
Fahrenheit, de -20 a 40 graus Celsius de 5 em 5.
'''

def Conversao_celsius_Fahrenheit():
    temperatura_celcius = -20
    tabela_conversão = []
    while temperatura_celcius < 40:
        celsius_to_fahrenheit = ((9*temperatura_celcius)/5)+32
        tabela_conversão.append(celsius_to_fahrenheit)
        temperatura_celcius += 5
    print(f'A tabela com as conversões de Graus Celcius para fahrenheit é: \n {tabela_conversão}')
