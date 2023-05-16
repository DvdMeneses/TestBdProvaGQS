from MockDb import MockBD
import sys

from queries_Aluno import ler_Turma_Aluno, escrever_Aluno_Media_MaiorNove, escrever_Aluno_Media
from queries_Turma import ler_Alunos_Turma

sys.path.insert(0, '..')
sys.path.insert(0, '../tests')



class TestAlunoBD(MockBD):
    def test_TurmasDoAluno(self):
        # turmas de um Aluno
        aluno1 = 'Carla'
        retorno = [('TAD0203',), ('TAD0201',), ('TAD0202',)]

        self.assertEqual(ler_Turma_Aluno(self.mock_db_config.get('bd'), aluno1), retorno)

    def test_Aluno_Media_MaiorNove(self):
        # RETORNAR ALUNOS COM NOTA MAIOR OU IGUAL A NOVE

        retorno = [('Carla',), ('Danilo',), ('Daniel',), ('David',), ('Davi',)]
        self.assertEqual(escrever_Aluno_Media_MaiorNove(self.mock_db_config.get('bd')), retorno)

    def test_Medias_Aluno(self):
        #RETORNA AS NOTAS DE UM ALUNO
        aluno1 = 'Carla'
        retorno = [(10,), (7,), (5,)]

        self.assertEqual(escrever_Aluno_Media(self.mock_db_config.get('bd'),aluno1), retorno)
