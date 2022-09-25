def mediaPonderada(n1,n2,peso1=1,peso2=1):
    """
     Esse programa calcula a média ponderada entre dois números n1 e n2,
    com seus respectivos pesos,peso1 e peso2, sendo que se esses pesos
    não forem fornecidos, terão valor igual a 1 como padrão.

    Nome: Estevão Soares Martins Loureiro
    DRE: 118045201

    """
    media_ponderada = (peso1*n1+peso2*n2)/(peso1+peso2)
    return media_ponderada

mediaPonderada(1,4)
mediaPonderada(1,4,1,1)
mediaPonderada(1,4,2,1)
mediaPonderada(1,4,2,2)
