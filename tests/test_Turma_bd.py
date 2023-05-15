from MockDb import MockBD
import sys

from TestBdProvaGQS.queries_Turma import ler_Alunos_Turma

sys.path.insert(0, '..')
sys.path.insert(0, '../tests')



class TestTurmaBD(MockBD):
    def test_AlunosDaTurma(self):
        # alunos da turma TAD0203
        turma1 = 'TAD0203'
        retorno = [('Carla',), ('Danilo',), ('Daniel',), ('David',), ('Davi',)]


        self.assertEqual(ler_Alunos_Turma(self.mock_db_config.get('bd'), turma1), retorno)
