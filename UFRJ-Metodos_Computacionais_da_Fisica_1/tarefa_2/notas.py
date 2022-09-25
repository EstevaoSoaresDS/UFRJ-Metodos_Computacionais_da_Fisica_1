from numpy import loadtxt
def notas_turma ():
    array_notas = loadtxt("notas.dat")
    numero_alunos = len(array_notas)
    soma_notas = 0
    media_notas = round(soma_notas/numero_alunos,1)
    alunos_aprovados_direto = 0
    alunos_reprovados_direto = 0
    porcentagem_aprovados_direto = alunos_aprovados_direto * (100/78)
    porcentagem_reprovados_direto = alunos_reprovados_direto * (100/78)
    aluno_n = 0
    while aluno_n < numero_alunos:
        soma_notas += array_notas[aluno_n]
        if array_notas[aluno_n] >= 7:
            alunos_aprovados_direto += 1
        elif array_notas[aluno_n] < 3:
            alunos_reprovados_direto += 1
        aluno_n +=1
    
    print (f'Número de alunos da turma é de {numero_alunos}.\n A média da turma é de {round(soma_notas/numero_alunos,1)}.\n {alunos_aprovados_direto} foram aprovados direto ({round(alunos_aprovados_direto * (100/78),1)}%)\n e {alunos_reprovados_direto} reprovaram direto ({round(alunos_reprovados_direto * (100/78),1)}%).'
