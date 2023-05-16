from conexao import *



def escrever_Aluno_Media_MaiorNove(bd):
    # Retorna alunos com nota maior ou igual nove

    query = "SELECT a.nome " \
            "FROM Aluno a, Media_turma_aluno m " \
            "WHERE m.id_aluno = a.id AND " \
            "m.media >= 9"
    return ler_bd(bd, query)

def ler_Turma_Aluno(bd, nome_aluno):
    # Turmas de um aluno  atraves do nome do aluno

    query = "SELECT t.codigo " \
            "FROM Aluno a, Media_turma_aluno m, Turma t " \
            "WHERE m.id_aluno = a.id AND " \
            "m.id_turma = t.id AND " \
            "a.nome = ?"

    return ler_bd(bd, query, (nome_aluno,))

def escrever_Aluno_Media(bd , nomeAluno):
    # RETORNA AS NOTAS DE UM ALUNO ESPECIFICO

    query = "SELECT m.media " \
            "FROM Aluno a, Media_turma_aluno m " \
            " WHERE m.id_aluno = a.id AND " \
            "a.nome = ?"
    return ler_bd(bd,query,(nomeAluno,))


