from tests.conexao import * 

def ler_Alunos_Turma(bd, id_Turma):
    query= "SELECT a.nome " \
            "FROM Aluno a, Media_turma_aluno m, Turma t" \
                    "m.id_aluno = a.id AND" \
                     "m.id_turma = t.id" \
                     "t.codigo = ?"
        
    return ler_bd(bd, query,(id_Turma,))
print("hello")