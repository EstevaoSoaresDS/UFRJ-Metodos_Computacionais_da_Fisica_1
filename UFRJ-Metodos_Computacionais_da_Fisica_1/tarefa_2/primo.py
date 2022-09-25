'''
  Código onde é pedido ao usuário um número inteiro positivo "n" e imprime
 se o mesmo é primo ou não.
'''
def primo():
    n=int(input('Digite um número inteiro e positivo, e retornaremos se o mesmo é primo ou não!\n'))
    if n==1:
        print('O número digitado não é primo.')
    else:
        contagem_dos_sem_resto = 0
        for i in range(1,n+1): # Aqui meu i vai assumir todos os valores de 1 até n+1.
            if n % i == 0: # Vou verificar quais números dividem sem dar resto.
                contagem_dos_sem_resto += 1
        if contagem_dos_sem_resto == 2:
            print('O número digitado é primo!')
        else:
            print('O número digitado não é primo!')
