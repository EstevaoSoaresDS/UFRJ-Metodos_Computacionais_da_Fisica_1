import numpy as np
import math
import scipy.integrate as integrate
'''
  Esse código calcula através do método dos Trapézios e do método de Simpson
 uma integral que multiplicada por um fator N de normalização, nos da o equilibrio
 térmico, onde a temperatura obedece a distribuição de Maxwell-Boltzmann, onde os
 limites de integração são de 0 à 2.
'''
def R_dividido_por_N(x):
    N=4*np.pi*(3/(2*np.pi))**1.5 #Fator de Normalização da distribuição Maxwell-Boltzmann
    return N*((x**2)*math.exp((-3*x**2)/2))
def trapezio(fun,a,b,k):
    Tk=0
    precisao_re=10**-6 #le-6 que é a precisão relativa desejada
    T=((b-a)/2)*(fun(a)+fun(b))
    for k in range(1,k):
        delta=(b-a)/2**k
        soma=0
        for j in range (1,2**k,2):
            soma+=fun(a+j*delta)
        Tk=(T/2)+delta*soma
        if fabs(Tk-T)/fabs(Tk)<precisao_re: #Se a presisão relativa calculada através de Tk e T for menor que a desejada
            break
        else:
            T=Tk #Caso contrario T recebe Tk
    return Tk
def simpson(fun,a,b,k):
    return trapezio(fun,a,b,k)+(trapezio(fun,a,b,k)-trapezio(fun,a,b,k-1))/3 # Forma abreviada para executar o método de Simpson através do método dos trapezios da função anterior

'''
 Implementando o item 4, onde vamos calcular a integral utilizando a biblioteca 
scipy do Python, utilizando o método quad.
'''
dI=integrate.quad(R_dividido_por_N,0,2)
dI
print(f" O valor da Integral utilizando o método squad do Scypy é {dI}\ne calculando pelo WolfranAlpha,temos: 0.992617.")
'''
 Vamos agora testar os dois métodos, tanto para k=100 quanto para k=2.
'''
maxwell_boltzmann_trapezio_100 = trapezio(fun=R_dividido_por_N,a=0,b=2,k=100)
maxwell_boltzmann_trapezio_100
print(f"Calculando pelo método do Trabézio, para k=100, temos:\n{maxwell_boltzmann_trapezio_100}")
maxwell_boltzmann_simpson_100 = simpson(fun=R_dividido_por_N,a=0,b=2,k=100)
maxwell_boltzmann_simpson_100
print(f"Calculando pelo método do Simpson, para k=100, temos:\n{maxwell_boltzmann_simpson_100}")
maxwell_boltzmann_trapezio_2 = trapezio(fun=R_dividido_por_N,a=0,b=2,k=2)
maxwell_boltzmann_trapezio_2
print(f"Calculando pelo método do Trabézio, para k=2, temos:\n{maxwell_boltzmann_trapezio_2}")
maxwell_boltzmann_simpson_2 = simpson(fun=R_dividido_por_N,a=0,b=2,k=2)
maxwell_boltzmann_simpson_2
print(f"Calculando pelo método do Simpson, para k=2, temos:\n{maxwell_boltzmann_simpson_2}")
