'''
Nome: Estevão Soares Martins Loureiro
DRE: 118045201
Métodos Computacionais da Física I
'''
import numpy as np
import matplotlib.pyplot as plt
'''
 A função taylor_cosseno calcula a série de Taylor em torno de x_0=0 para N termos
para um determinado x.
'''


def taylor_cosseno(x, N):
    cossenox = 0
    for N in range(0, N+1):
        cosseno1 = (-1)**N
        cosseno2 = np.math.factorial(2*N)
        cosseno3 = x**(2*N)
        cossenox += x**(2*N)*(((-1)**N)/np.math.factorial(2*N))
    return cossenox


# Imprimindo o que se pede para pi/6:
valor_exato_cosseno_1 = np.cos(np.pi/6)
taylort_1_N2 = taylor_cosseno(np.pi/6, 2)
taylort_1_N4 = taylor_cosseno(np.pi/6, 4)
taylort_1_N6 = taylor_cosseno(np.pi/6, 6)
print(f'Esses são os valores aproximados do cosseno de pi/6 para 2,4 e 6 \ntermos respectivamente:\n{taylort_1_N2}\n{taylort_1_N4}\n{taylort_1_N6}')
diferença_1_N2 = valor_exato_cosseno_1-taylort_1_N2
diferença_1_N4 = valor_exato_cosseno_1-taylort_1_N4
diferença_1_N6 = valor_exato_cosseno_1-taylort_1_N6
print(f'Essa é a diferença entre o valor exato obtido pelo módulo cos do numpy\ne o valor obtido na função taylor_cosseno para 2,4,6 termos respectivamente:\n{diferença_1_N2}\n{diferença_1_N4}\n{diferença_1_N6}\n')
taylort_1_N2_proximo_termo = taylor_cosseno(
    np.pi/6, 3)-taylor_cosseno(np.pi/6, 2)
taylort_1_N4_proximo_termo = taylor_cosseno(
    np.pi/6, 5)-taylor_cosseno(np.pi/6, 4)
taylort_1_N6_proximo_termo = taylor_cosseno(
    np.pi/6, 7)-taylor_cosseno(np.pi/6, 6)
print(f'Esses são os termos posteriores ao termo N para N=2,4,6 respectivamente:\n{taylort_1_N2_proximo_termo}\n{taylort_1_N4_proximo_termo}\n{taylort_1_N6_proximo_termo}\n')
# Imprimindo o que se pede para 3pi/4:
valor_exato_cosseno_2 = np.cos(3*np.pi/4)
taylort_2_N2 = taylor_cosseno(3*np.pi/4, 2)
taylort_2_N4 = taylor_cosseno(3*np.pi/4, 4)
taylort_2_N6 = taylor_cosseno(3*np.pi/4, 6)
print(f'Esses são os valores aproximados do cosseno de 3pi/4 para 2,4 e 6 \ntermos respectivamente:\n{taylort_2_N2}\n{taylort_2_N4}\n{taylort_2_N6}')
diferença_2_N2 = valor_exato_cosseno_2-taylort_2_N2
diferença_2_N4 = valor_exato_cosseno_2-taylort_2_N4
diferença_2_N6 = valor_exato_cosseno_2-taylort_2_N6
print(f'Essa é a diferença entre o valor exato obtido pelo módulo cos do numpy\ne o valor obtido na função taylor_cosseno para 2,4,6 termos respectivamente:\n{diferença_2_N2}\n{diferença_2_N4}\n{diferença_2_N6}\n')
taylort_2_N2_proximo_termo = taylor_cosseno(
    3*np.pi/4, 3)-taylor_cosseno(3*np.pi/4, 2)
taylort_2_N4_proximo_termo = taylor_cosseno(
    3*np.pi/4, 5)-taylor_cosseno(3*np.pi/4, 4)
taylort_2_N6_proximo_termo = taylor_cosseno(
    3*np.pi/4, 7)-taylor_cosseno(3*np.pi/4, 6)
print(f'Esses são os termos posteriores ao termo N para N=2,4,6 respectivamente:\n{taylort_2_N2_proximo_termo}\n{taylort_2_N4_proximo_termo}\n{taylort_2_N6_proximo_termo}\n')
# Observamos uma discrepância na ordem de grandeza muito grande entre o termo 4 da série e o termo 6, sendo uma diferença de ordem de 10^-3.
# Gráfico:
x = np.arange(-np.pi/12, np.pi, 0.1)
y_cos_numpy = np.cos(x)
y_cos_N2 = taylor_cosseno(x, 2)
y_cos_N4 = taylor_cosseno(x, 4)
y_cos_N6 = taylor_cosseno(x, 6)
plt.grid()
plt.plot(x, y_cos_numpy, linewidth=3.0, linestyle='--', color='r')
plt.plot(x, y_cos_N2, linewidth=2.0, linestyle='-', color='g')
plt.plot(x, y_cos_N4, linewidth=2.0, linestyle='-', color='k')
plt.plot(x, y_cos_N6, linewidth=2.0, linestyle='-', color='b')
plt.xlabel('x(graus)')
plt.ylabel('cos(x)')
plt.title('Serie de Taylor - cos(x)')
