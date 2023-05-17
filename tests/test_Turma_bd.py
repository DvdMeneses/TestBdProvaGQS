from MockDb import MockBD
import sys

from queries_Turma import ler_Medias_Turma

sys.path.insert(0, '..')
sys.path.insert(0, '../tests')



class TestTurmaBD(MockBD):

    def test_MediasDaTurma(self):
        #MAIOR MEDIA DE UMA TURMA  (TAD0203)
        #QUESTAO 1
        turma1 = 'TAD0203'
        retorno1 = [(10,)]# TURMA TAD0203 COM NOTA 10 COMO A MAXIMA E RPETIDA

        turma2 = 'TAD0202'
        retorno2 = [(8,)] # TURMA TAD0202 COM NOTA COMO MAXIMA E NAO SE RPETE

        turma3 = 'TAD0204'
        retorno3 = [(None,)] # TURMA TAD0204 NAO TEM ALUNO CADASTRADO

        self.assertEqual(ler_Medias_Turma(self.mock_db_config.get('bd'), turma1), retorno1)
        self.assertEqual(ler_Medias_Turma(self.mock_db_config.get('bd'), turma2), retorno2)
        self.assertEqual(ler_Medias_Turma(self.mock_db_config.get('bd'), turma3), retorno3)


    # def test_AlunosDaTurma(self):
    #     # alunos da turma TAD0203
    #     turma1 = 'TAD0203'
    #     retorno = [('Carla',), ('Danilo',), ('Daniel',), ('David',), ('Davi',)]
    #
    #
    #     self.assertEqual(ler_Alunos_Turma(self.mock_db_config.get('bd'), turma1), retorno)





