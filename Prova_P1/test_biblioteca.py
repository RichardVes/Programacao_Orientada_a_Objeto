import unittest
from biblioteca import (Livro, Aluno, Professor, Biblioteca,
                      LimiteEmprestimosExcedido, LivroIndisponivel,
                      UsuarioNaoEncontrado, LivroNaoEncontrado)

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para todos os testes"""
        self.biblioteca = Biblioteca()
        
        # Adicionar livros
        self.livro1 = Livro("LIV001", "Python 101", "Autor A", True)
        self.livro2 = Livro("LIV002", "OOP Principles", "Autor B", True)
        self.livro3 = Livro("LIV003", "Design Patterns", "Autor C", True)
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)
        self.biblioteca.adicionar_livro(self.livro3)
        
        # Cadastrar usuários
        self.aluno1 = Aluno("ALU001", "João Silva")
        self.aluno2 = Aluno("ALU002", "Maria Souza")
        self.prof1 = Professor("PRO001", "Carlos Oliveira")
        self.biblioteca.cadastrar_usuario(self.aluno1)
        self.biblioteca.cadastrar_usuario(self.aluno2)
        self.biblioteca.cadastrar_usuario(self.prof1)
    
    def test_adicionar_livro(self):
        """Testa a adição de livros ao acervo"""
        self.assertEqual(len(self.biblioteca.acervo), 3)
        novo_livro = Livro("LIV004", "New Book", "Autor D", True)
        self.biblioteca.adicionar_livro(novo_livro)
        self.assertEqual(len(self.biblioteca.acervo), 4)
        self.assertIn(novo_livro, self.biblioteca.acervo)
    
    def test_cadastrar_usuario(self):
        """Testa o cadastro de usuários"""
        self.assertEqual(len(self.biblioteca.usuarios_cadastrados), 3)
        novo_aluno = Aluno("ALU003", "Novo Aluno")
        self.biblioteca.cadastrar_usuario(novo_aluno)
        self.assertEqual(len(self.biblioteca.usuarios_cadastrados), 4)
        self.assertIn(novo_aluno, self.biblioteca.usuarios_cadastrados)
    
    def test_emprestimo_aluno_sucesso(self):
        """Testa empréstimo bem-sucedido para aluno"""
        # Aluno pode pegar até 3 livros
        self.biblioteca.registrar_emprestimo("ALU001", "LIV001")
        self.biblioteca.registrar_emprestimo("ALU001", "LIV002")
        
        aluno = self.biblioteca.usuarios_cadastrados[0]
        self.assertEqual(len(aluno.lista_livros_emprestados), 2)
        self.assertFalse(self.livro1.disponivel)
        self.assertFalse(self.livro2.disponivel)
    
    def test_emprestimo_aluno_limite_excedido(self):
        """Testa limite de empréstimos para aluno"""
        # Aluno pega 3 livros (limite)
        self.biblioteca.registrar_emprestimo("ALU001", "LIV001")
        self.biblioteca.registrar_emprestimo("ALU001", "LIV002")
        self.biblioteca.registrar_emprestimo("ALU001", "LIV003")
        
        # Tentativa de pegar o 4º livro deve falhar
        with self.assertRaises(LimiteEmprestimosExcedido):
            self.biblioteca.registrar_emprestimo("ALU001", "LIV001")
    
    def test_emprestimo_professor_sucesso(self):
        """Testa empréstimo bem-sucedido para professor"""
        # Professor pode pegar até 5 livros
        for i in range(1, 6):
            isbn = f"LIV00{i}" if i < 4 else f"LIV00{i-3}"  # Reutiliza livros para teste
            try:
                self.biblioteca.registrar_emprestimo("PRO001", isbn)
            except LivroIndisponivel:
                pass  # Ignora se livro já está emprestado
        
        professor = self.biblioteca.usuarios_cadastrados[2]
        self.assertEqual(len(professor.lista_livros_emprestados), 3)  # Só temos 3 livros
    
    def test_emprestimo_livro_indisponivel(self):
        """Testa tentativa de pegar livro indisponível"""
        self.biblioteca.registrar_emprestimo("ALU001", "LIV001")  # Aluno pega livro
        
        # Outro usuário tenta pegar o mesmo livro
        with self.assertRaises(LivroIndisponivel):
            self.biblioteca.registrar_emprestimo("ALU002", "LIV001")
    
    def test_devolucao_sucesso(self):
        """Testa devolução bem-sucedida"""
        self.biblioteca.registrar_emprestimo("ALU001", "LIV001")
        self.assertFalse(self.livro1.disponivel)
        
        self.biblioteca.registrar_devolucao("ALU001", "LIV001")
        self.assertTrue(self.livro1.disponivel)
        self.assertEqual(len(self.aluno1.lista_livros_emprestados), 0)
    
    def test_devolucao_livro_nao_emprestado(self):
        """Testa tentativa de devolver livro não emprestado"""
        with self.assertRaises(LivroNaoEncontrado):
            self.biblioteca.registrar_devolucao("ALU001", "LIV001")
    
    def test_consultar_livros_emprestados(self):
        """Testa a consulta de livros emprestados"""
        # Nenhum livro emprestado inicialmente
        self.assertEqual(len(self.biblioteca.consultar_livros_emprestados()), 0)
        
        # Realiza alguns empréstimos
        self.biblioteca.registrar_emprestimo("ALU001", "LIV001")
        self.biblioteca.registrar_emprestimo("PRO001", "LIV002")
        
        emprestados = self.biblioteca.consultar_livros_emprestados()
        self.assertEqual(len(emprestados), 2)
        
        # Verifica os dados dos empréstimos
        self.assertEqual(emprestados[0]['usuario'], "João Silva")
