import sys

from MockDb import MockBD
from queries_Aluno import escrever_Turma_Media_MaiorNove, ler_Turma_Aluno

sys.path.insert(0, '..')
sys.path.insert(0, '../tests')



class TestAlunoBD(MockBD):


    def test_Turmas_MediaMaiorNove(self):
        # Test questao 4

        retorno = [('TAD0203',)]# SO HA UM RETORNO
        self.assertEqual(escrever_Turma_Media_MaiorNove(self.mock_db_config.get('bd')), retorno)

    def test_TurmasDoAluno(self):
        # turmas de um Aluno
        aluno1 = 'Carla' # ALUNO COM MAIS DE UMA TURMA
        retorno1 = [(3,)]

        aluno2 = 'Alice'# ALUNO EM NEM UMA TURMA
        retorno2 = [(0,)]



        self.assertEqual(ler_Turma_Aluno(self.mock_db_config.get('bd'), aluno1), retorno1)
        self.assertEqual(ler_Turma_Aluno(self.mock_db_config.get('bd'), aluno2), retorno2)

# FUNCTION DE APOIO FEITA ANTES

    # def test_Medias_Aluno(self):
    #     #RETORNA AS NOTAS DE UM ALUNO
    #     aluno1 = 'Carla'
    #     retorno = [(10,), (7,), (5,)]
    #
    #     self.assertEqual(escrever_Aluno_Media(self.mock_db_config.get('bd'),aluno1), retorno)


