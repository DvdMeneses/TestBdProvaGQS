from TestBdProvaGQS.conexao import *


def ler_Alunos_Turma(bd, id_Turma):
    query = "SELECT a.nome " \
            "FROM Aluno a, Media_turma_aluno m, Turma t " \
            "WHERE m.id_aluno = a.id AND " \
            "m.id_turma = t.id AND " \
            "t.codigo = ?"

    return ler_bd(bd, query, (id_Turma,))

