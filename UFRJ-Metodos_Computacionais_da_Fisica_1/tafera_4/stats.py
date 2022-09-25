import numpy as np
def stats(entrada):
"""
  O programa a seguir pede uma entrada array, e imprime na tela o número
de elementos,o maior e o menor deles, a soma dos mesmo, média e desvio padrão.

 Nome: Estevão Soares Martins Loureiro
 DRE: 118045201
""" 
  if type(entrada) == np.ndarray:
    numero_elementos_array=len(entrada)
    array_sort=np.sort(entrada)
    menor_elemento=array_sort[0]
    maior_elemento=array_sort[-1]
    soma=0
    for elemento in entrada:
      soma +=elemento
    media = round(soma/numero_elementos_array,3)
    desvio_padrao = round(np.std(entrada),3)
    print(f'\n A entrada array fornecida tem {numero_elementos_array} elementos, sendo o menor deles {menor_elemento} e o maior {maior_elemento}, \na soma dos elementos é {soma}, a media {media} e o desvio padrão {desvio_padrao}.')
    #return numero_elementos_array,menor_elemento,maior_elemento,soma,media,desvio_padrao
  else:
    print('\n A entrada fornecida não é um array!')

stats(np.array([1,9,7,6,2,7]))

stats([1,9,7,6,2,7])

stats(np.array([0]))
