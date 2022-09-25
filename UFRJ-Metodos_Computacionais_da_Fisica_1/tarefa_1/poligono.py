'''
  Programa onde é dado o valor L que é o comprimento da interseção entre
os triangulos isósceles e um poligono de N lados, onde é possível calcular
a Área do poligono sabendo o valor de L
'''
from math import tan,pi
def área_poligono(L):
    N=6
    Área=round(N*L**2/(4*tan(pi/N)),3)
    print(f"A área do poligono é de {Área} u^2")
    return Área
