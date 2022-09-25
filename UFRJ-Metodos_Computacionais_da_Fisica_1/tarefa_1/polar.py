'''
 Programa que dado as coordenadas cartesianas no R2, nos retorna 
em coordenadas polares
'''
from math import atan,degrees
def polar(coordenadaX,coordenadaY):
    raio=(coordenadaX**2+coordenadaY**2)
    angulo_radianos=round(atan(coordenadaX/coordenadaY),3)
    angulo_graus=int(degrees(angulo_radianos))
    print (f' O raio é de {raio} unidade, o ângulo em radianos é de {angulo_radianos} rad, e em graus de {angulo_graus} graus.')
    