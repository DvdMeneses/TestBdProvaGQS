from unittest import TestCase
from TestBdProvaGQS.conexao import *

import sys
sys.path.insert(0, '.')

BD = "TestDB.db"

class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()

        # Medico: id(PK), nome, crm, especialidade
        # Paciente: id (PK), nome
        # Prontuario: id (PK), id_medico (FK), id_paciente(FK)
        # Exames: id (PK), nome, id_prontuario (FK), resultado

        query_create_Professor = """CREATE TABLE Professor (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL
                                )"""
        query_create_Aluno = """CREATE TABLE Aluno (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL
                                )"""
        query_create_Turma = """CREATE TABLE Turma (
                                  id int NOT NULL PRIMARY KEY,
                                  nome text NOT NULL,
                                  codigo text NOT NULL
                                )"""
        query_create_Media_aluno_turma = """CREATE TABLE Media_turma_aluno (
                                  id int NOT NULL PRIMARY KEY,
                                  id_turma int,
                                  id_aluno int,
                                  nota1 float,
                                  nota2 float,
                                  nota3 float,
                                  media float,
                                  
                                  FOREIGN KEY (id_turma) REFERENCES Turma(id),
                                  FOREIGN KEY (id_aluno) REFERENCES Aluno(id)
                                 
                                )"""
        try:
            cursor.execute(query_create_Professor)
            cursor.execute(query_create_Aluno)
            cursor.execute(query_create_Turma)
            cursor.execute(query_create_Media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_insert_Professor = """INSERT INTO Professor (id, nome) VALUES
                                    (1, 'Guilherme'),
                                    (2, 'Sarah'),
                                    (3, 'Melissa'),
                                    (4, 'Gisele')"""

        query_insert_Aluno = """INSERT INTO Aluno (id, nome) VALUES
                                    (1, 'Carla'),
                                    (2, 'Danilo'),
                                    (3, 'Daniel'),
                                    (4, 'David'),
                                    (5, 'Davi'),
                                    (6, 'Alice')"""

        query_insert_Turma = """INSERT INTO Turma (id, nome, codigo) VALUES
                                    (1, 2020.1, 'TAD0201'),
                                    (2, 2021.1, 'TAD0202'),
                                    (3, 2022.1, 'TAD0203'),
                                    (4, 2023.1, 'TAD0204')
                                    """

        query_insert_Media_aluno_turma = """INSERT INTO Media_aluno_turma (id, id_turma, id_aluno, nota1, nota2, nota3, media) VALUES
                                    (1, 3, 1, 10, 10, 10, 10),
                                    (2, 3, 2, 9.5, 9.5, 9.5, 9.5),
                                    (3, 3, 3, 9.0, 9.0, 9.0, 9.0),
                                    (4, 3, 4, 10, 10, 10, 10),
                                    (5, 3, 5, 10, 10, 10, 10),
                                    (6, 1, 1, 7, 7, 7, 7),
                                    (7, 2, 1, 5, 5, 5, 5),
                                    (8, 2, 3, 0, 0, 0, 0),
                                    (9, 1, 4, 8, 8, 8, 8),
                                    (10,2, 5, 8, 8, 8, 8)
                                    """
        # aluno 6 nao esta em nem uma turma e turma 4 nao tem nem um aluno 
        try:
            cursor.execute(query_insert_Professor)
            cursor.execute(query_insert_Aluno)
            cursor.execute(query_insert_Turma)
            cursor.execute(query_insert_Media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()

        desconectar(con)

        testconfig ={
            'bd': BD
        }
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()

        try:
            cursor.execute("DROP TABLE Professor")
            cursor.execute("DROP TABLE Aluno")
            cursor.execute("DROP TABLE Turma")
            cursor.execute("DROP TABLE Media_aluno_turma")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)
