from aluno import *

import unittest

class test_aluno(unittest.TestCase):
    def test_maior_nota(self):
        situacao1 =  [('Carla', 9.7),('Danilo', 6.7), ('Daniel', 3.4), ('Alice', 9.7), ('Flávio',5.7), ('Silvia', 4.4)]#com mais de um aluno com maior nota
        situacao2 = [('Carla', 2.0),('Danilo', 6.7), ('Daniel', 3.4), ('Alice', 3.7), ('Flávio',9.7), ('Silvia', 0)]#com um aluno com maior nota
        retorno1 = ['Carla', 'Alice']
        retorno2 = ['Flávio']
        self.assertEqual(Alunos_MaiorNota(situacao1), retorno1)
        self.assertEqual(Alunos_MaiorNota(situacao2), retorno2)




    def test_media_notas_por_professor(self):
        lista_notas1 = [('TAD0055', 1, 9.7), ('TAD0010', 2, 6.7), ('TAD0105', 3, 3.4),
                        ('TAD0105', 1, 4.4), ('TAD0105', 2, 7.1), ('TAD0027', 2, 9.7),
                        ('TAD0202', 3, 5.7), ('TAD0001', 3, 4.4)]

        resultado_esperado1 = {1: 7.05, 2: 7.83, 3: 4.5}

        self.assertEqual(media_notas_por_professor(lista_notas1), resultado_esperado1)



    def test_percentual_turmas_acima_sete(self):
        lista_medias1 = [('TAD0055', 1, 9.7), ('TAD0010', 2, 6.7), ('TAD0105', 3, 3.4),
                         ('TAD0105', 1, 4.4), ('TAD0105', 2, 7.1), ('TAD0027', 2, 9.7),
                         ('TAD0202', 3, 5.7), ('TAD0001', 3, 4.4)]

        resultado_esperado1 = {1: 50.0, 2: 66.67, 3: 0.0}

        self.assertEqual(percentual_turmas_acima_sete(lista_medias1), resultado_esperado1)

    def test_Aluno_Rendimento(self):
    #(['TAD0055', 'TAD0010', 'TAD0002', 'TAD0001', 'TAD1002', 'TAD0100', 'TAD0027', 'TAD0105', 'TAD0202', 'TAD2030'])


        historico1 = [('TAD0055', 1.7), ('TAD0010', 3.7), ('TAD0002', 3.4), ('TAD0001', 4.4), ('TAD1002', 5.1),
                     ('TAD0100', 2.7), ('TAD0027', 5.7), ('TAD0105', 4.4), ('TAD0202', 3.0),('TAD1002',2.0) ]#reprovou em tudo mas pagou todas

        retorno1 = (['TAD0055', 'TAD0010', 'TAD0002', 'TAD0001', 'TAD1002', 'TAD0100', 'TAD0027', 'TAD0105', 'TAD0202', 'TAD2030'])

        historico2 = [('TAD0055', 9.7), ('TAD0010', 9.7), ('TAD0002', 9.4), ('TAD0001', 9.4), ('TAD1002', 9.1),
                     ('TAD0100', 9.7), ('TAD0027', 9.7), ('TAD0105', 9.4), ('TAD0202', 9.0),('TAD1002',9.0), ('TAD2030', 10) ]

        retorno2 = ([])




        self.assertEqual(disciplinas_pendentesParaAluno(historico1), retorno1)

        self.assertEqual(disciplinas_pendentesParaAluno(historico2), retorno2)
