from MockDb import MockBD
import sys

from queries_Turma import ler_Alunos_Turma, ler_Medias_Turma

sys.path.insert(0, '..')
sys.path.insert(0, '../tests')



class TestTurmaBD(MockBD):
    def test_AlunosDaTurma(self):
        # alunos da turma TAD0203
        turma1 = 'TAD0203'
        retorno = [('Carla',), ('Danilo',), ('Daniel',), ('David',), ('Davi',)]


        self.assertEqual(ler_Alunos_Turma(self.mock_db_config.get('bd'), turma1), retorno)

    def test_MediasDaTurma(self):
        #medias da turma TAD0203
        turma1 = 'TAD0203'
        retorno = [(10,), (9.5,), (9.0,), (10,), (10,)]

        self.assertEqual(ler_Medias_Turma(self.mock_db_config.get('bd'), turma1), retorno)






