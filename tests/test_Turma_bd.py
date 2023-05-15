from MockDb import MockBD

import sys
sys.path.insert(0,'..')

from tests.conexao import *
from queries_Turma import *

class TestTurmaBD(MockBD):
    def test_AlunosDaTurma(self):
        #alunos da turma TAD0203
        turma1 = 'TAD0203'
        retorno = [('Carla',),('Danilo',),('Daniel',)]

        self.assertEqual(TestTurmaBD(self.mock_db_config.get('bd'), turma1),retorno)
