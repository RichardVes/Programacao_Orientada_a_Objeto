from abc import ABC, abstractmethod

# Exceções personalizadas
class LimiteEmprestimosExcedido(Exception):
    pass

class LivroIndisponivel(Exception):
    pass

class UsuarioNaoEncontrado(Exception):
    pass

class LivroNaoEncontrado(Exception):
    pass

# Classe Livro
class Livro:
    def __init__(self, isbn: str, titulo: str, autor: str, disponivel: bool = True):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = disponivel
    
    @property
    def isbn(self):
        return self.__isbn
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def disponivel(self):
        return self.__disponivel
    
    def emprestar(self):
        if not self.__disponivel:
            raise LivroIndisponivel(f"O livro {self.__titulo} não está disponível para empréstimo")
        self.__disponivel = False
    
    def devolver(self):
        self.__disponivel = True
    
    def __str__(self):
        return f"Livro(ISBN: {self.__isbn}, Título: {self.__titulo}, Autor: {self.__autor}, Disponível: {self.__disponivel})"

# Classe Usuário (Abstrata)
class Usuario(ABC):
    def __init__(self, matricula: str, nome: str):
        self.__matricula = matricula
        self.__nome = nome
        self.__lista_livros_emprestados = []
    
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def lista_livros_emprestados(self):
        return self.__lista_livros_emprestados
    
    @abstractmethod
    def pegar_emprestado(self, livro: Livro):
        pass
    
    @abstractmethod
    def devolver_livro(self, livro: Livro):
        pass
    
    @property
    @abstractmethod
    def limite_emprestimos(self):
        pass
    
    def __str__(self):
        return f"Usuário(Matrícula: {self.__matricula}, Nome: {self.__nome}, Tipo: {self.__class__.__name__}, Livros Emprestados: {len(self.__lista_livros_emprestados)}/{self.limite_emprestimos})"

# Classe Aluno
class Aluno(Usuario):
    @property
    def limite_emprestimos(self):
        return 3
    
    def pegar_emprestado(self, livro: Livro):
        if len(self.lista_livros_emprestados) >= self.limite_emprestimos:
            raise LimiteEmprestimosExcedido(f"Aluno {self.nome} atingiu o limite de {self.limite_emprestimos} empréstimos")
        livro.emprestar()
        self.lista_livros_emprestados.append(livro)
    
    def devolver_livro(self, livro: Livro):
        if livro in self.lista_livros_emprestados:
            livro.devolver()
            self.lista_livros_emprestados.remove(livro)
        else:
            raise LivroNaoEncontrado(f"Livro {livro.titulo} não encontrado na lista de empréstimos do aluno")

# Classe Professor
class Professor(Usuario):
    @property
    def limite_emprestimos(self):
        return 5
    
    def pegar_emprestado(self, livro: Livro):
        if len(self.lista_livros_emprestados) >= self.limite_emprestimos:
            raise LimiteEmprestimosExcedido(f"Professor {self.nome} atingiu o limite de {self.limite_emprestimos} empréstimos")
        livro.emprestar()
        self.lista_livros_emprestados.append(livro)
    
    def devolver_livro(self, livro: Livro):
        if livro in self.lista_livros_emprestados:
            livro.devolver()
            self.lista_livros_emprestados.remove(livro)
        else:
            raise LivroNaoEncontrado(f"Livro {livro.titulo} não encontrado na lista de empréstimos do professor")

# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.__acervo = []
        self.__usuarios_cadastrados = []
    
    @property
    def acervo(self):
        return self.__acervo
    
    @property
    def usuarios_cadastrados(self):
        return self.__usuarios_cadastrados
    
    def cadastrar_usuario(self, usuario: Usuario):
        self.__usuarios_cadastrados.append(usuario)
    
    def registrar_emprestimo(self, matricula: str, isbn: str):
        usuario = self.__buscar_usuario(matricula)
        livro = self.__buscar_livro(isbn)
        
        usuario.pegar_emprestado(livro)
        return f"Empréstimo registrado: {livro.titulo} para {usuario.nome}"
    
    def registrar_devolucao(self, matricula: str, isbn: str):
        usuario = self.__buscar_usuario(matricula)
        livro = self.__buscar_livro(isbn)
        
        usuario.devolver_livro(livro)
        return f"Devolução registrada: {livro.titulo} por {usuario.nome}"
    
    def consultar_livros_emprestados(self):
        livros_emprestados = []
        for usuario in self.__usuarios_cadastrados:
            for livro in usuario.lista_livros_emprestados:
                livros_emprestados.append({
                    'usuario': usuario.nome,
                    'matricula': usuario.matricula,
                    'tipo': usuario.__class__.__name__,
                    'livro': livro.titulo,
                    'isbn': livro.isbn
                })
        return livros_emprestados
    
    def adicionar_livro(self, livro: Livro):
        self.__acervo.append(livro)
    
    def __buscar_usuario(self, matricula: str) -> Usuario:
        for usuario in self.__usuarios_cadastrados:
            if usuario.matricula == matricula:
                return usuario
        raise UsuarioNaoEncontrado(f"Usuário com matrícula {matricula} não encontrado")
    
    def __buscar_livro(self, isbn: str) -> Livro:
        for livro in self.__acervo:
            if livro.isbn == isbn:
                return livro
        raise LivroNaoEncontrado(f"Livro com ISBN {isbn} não encontrado no acervo")
    
    def __str__(self):
        return f"Biblioteca(Acervo: {len(self.__acervo)} livros, Usuários: {len(self.__usuarios_cadastrados)})"

# Função para popular a biblioteca com dados iniciais
def popular_biblioteca():
    # Criar biblioteca
    biblioteca = Biblioteca()
    
    # Adicionar livros ao acervo
    livros = [
        Livro("LIV001", "Titulo 1", "Autor 1", True),
        Livro("LIV002", "Titulo 2", "Autor 2", True),
        Livro("LIV003", "Titulo 3", "Autor 3", True),
        Livro("LIV004", "Titulo 4", "Autor 4", True),
        Livro("LIV005", "Titulo 5", "Autor 5", True)
    ]
    
    for livro in livros:
        biblioteca.adicionar_livro(livro)
    
    # Cadastrar usuários
    alunos = [
        Aluno("ALUNOXX1", "Nome 1"),
        Aluno("ALUNOXX2", "Nome 2")
    ]
    
    professores = [
        Professor("PROFXX1", "Professor")
    ]
    
    for aluno in alunos:
        biblioteca.cadastrar_usuario(aluno)
    
    for professor in professores:
        biblioteca.cadastrar_usuario(professor)
    
    return biblioteca

# Exemplo de uso do sistema
def main():
    biblioteca = popular_biblioteca()
    
    print("=== Sistema de Biblioteca Universitária ===")
    print(biblioteca)
    print("\nUsuários cadastrados:")
    for usuario in biblioteca.usuarios_cadastrados:
        print(usuario)
    
    print("\nLivros disponíveis:")
    for livro in biblioteca.acervo:
        print(livro)
    
    # Testar empréstimos
    try:
        print("\nRealizando empréstimos:")
        # Aluno pega 2 livros
        print(biblioteca.registrar_emprestimo("ALUNOXX1", "LIV001"))
        print(biblioteca.registrar_emprestimo("ALUNOXX1", "LIV002"))
        
        # Professor pega 1 livro
        print(biblioteca.registrar_emprestimo("PROFXX1", "LIV003"))
        
        # Tentar pegar livro indisponível (deve falhar)
        try:
            print(biblioteca.registrar_emprestimo("ALUNOXX2", "LIV001"))
        except LivroIndisponivel as e:
            print(f"Erro: {e}")
        
        # Aluno tentar pegar mais livros que o limite (deve falhar no 4º)
        print(biblioteca.registrar_emprestimo("ALUNOXX1", "LIV004"))  # 3º livro (limite)
        try:
            print(biblioteca.registrar_emprestimo("ALUNOXX1", "LIV005"))  # Deve falhar
        except LimiteEmprestimosExcedido as e:
            print(f"Erro: {e}")
        
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    # Consultar livros emprestados
    print("\nLivros emprestados atualmente:")
    emprestados = biblioteca.consultar_livros_emprestados()
    for emp in emprestados:
        print(f"{emp['usuario']} ({emp['tipo']}): {emp['livro']} (ISBN: {emp['isbn']})")
    
    # Testar devoluções
    try:
        print("\nRealizando devoluções:")
        print(biblioteca.registrar_devolucao("ALUNOXX1", "LIV001"))
        print(biblioteca.registrar_devolucao("PROFXX1", "LIV003"))
        
        # Consultar livros emprestados após devoluções
        print("\nLivros emprestados após devoluções:")
        emprestados = biblioteca.consultar_livros_emprestados()
        for emp in emprestados:
            print(f"{emp['usuario']} ({emp['tipo']}): {emp['livro']} (ISBN: {emp['isbn']})")
        
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()