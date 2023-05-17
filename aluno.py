def Alunos_MaiorNota(listaAlunos):
    resultado = []
    max_notas = listaAlunos[0][1]
    for elem in listaAlunos:
        if (elem[1] == max_notas):
            resultado.append(elem[0])
        elif (elem[1] > max_notas):
            max_notas = elem[1]
            resultado = []
            resultado.append(elem[0])
    return resultado


def media_notas_por_professor(lista_notas):
    notas_por_professor = {}
    contador_por_professor = {}

    for turma, id_professor, media in lista_notas:
        if id_professor in notas_por_professor:
            notas_por_professor[id_professor] += media
            contador_por_professor[id_professor] += 1
        else:
            notas_por_professor[id_professor] = media
            contador_por_professor[id_professor] = 1

    medias_por_professor = {}
    for id_professor, soma_notas in notas_por_professor.items():
        contador = contador_por_professor[id_professor]
        media = soma_notas / contador
        medias_por_professor[id_professor] = round(media, 2)

    return medias_por_professor


def percentual_turmas_acima_sete(lista_medias):
    turmas_acima_sete = {}
    total_turmas_por_professor = {}

    for turma, id_professor, media in lista_medias:
        if id_professor in turmas_acima_sete:
            if media > 7.0:
                turmas_acima_sete[id_professor] += 1
            total_turmas_por_professor[id_professor] += 1
        else:
            if media > 7.0:
                turmas_acima_sete[id_professor] = 1
            else:
                turmas_acima_sete[id_professor] = 0
            total_turmas_por_professor[id_professor] = 1

    percentuais = {}
    for id_professor, turmas_acima in turmas_acima_sete.items():
        total_turmas = total_turmas_por_professor[id_professor]
        percentual = (turmas_acima / total_turmas) * 100
        percentuais[id_professor] = round(percentual, 2)

    return percentuais



def disciplinas_pendentesParaAluno(historico_notas):
    disciplinas_pendentes = []
    disciplinas_aprovadas = []
    disciplinas_totais = [('TAD0055'), ('TAD0010'), ('TAD0002'), ('TAD0001'), ('TAD1002'), ('TAD0100'), ('TAD0027'), ('TAD0105'), ('TAD0202'), ('TAD2030')]

    for elem in historico_notas:
        if elem[1] >= 7:
            disciplinas_aprovadas.append(elem[0])

    for elem in disciplinas_totais:
        if elem not in disciplinas_aprovadas:
            disciplinas_pendentes.append(elem)


    return disciplinas_pendentes
