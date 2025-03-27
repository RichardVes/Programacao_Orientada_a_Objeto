# Exercício de Prova – Programação Orientada a Objetos (POO)

**Tema: Sistema de Gerenciamento de Biblioteca Universitária**

## Enunciado

Você foi contratado para desenvolver um sistema de gerenciamento para uma biblioteca universitária. O sistema deve permitir o cadastro de livros, usuários (alunos e professores) e empréstimos, seguindo os princípios de POO.

---

## **Requisitos:**

### **1. Classe `Livro`**

- **Atributos:**
  - `ISBN` (string)
  - `título` (string)
  - `autor` (string)
  - `disponível` (boolean)
- **Métodos:**
  - `emprestar()`: marca o livro como indisponível.
  - `devolver()`: marca o livro como disponível.

### **2. Classe `Usuario` (Abstrata)**

- **Atributos:**
  - `matricula` (string)
  - `nome` (string)
  - `lista_livros_emprestados` (lista de `Livro`)
- **Métodos abstratos:**
  - `pegar_emprestado(livro: Livro)`: adiciona o livro à lista de empréstimos.
  - `devolver_livro(livro: Livro)`: remove o livro da lista.

### **3. Classes `Aluno` e `Professor` (Herança)**

- **`Aluno`:**
  - Limite de **3 livros** emprestados simultaneamente.
- **`Professor`:**
  - Limite de **5 livros** emprestados simultaneamente.
- _Implemente os métodos abstratos da classe pai._

### **4. Classe `Biblioteca`**

- **Atributos:**
  - `acervo` (lista de `Livro`)
  - `usuarios_cadastrados` (lista de `Usuario`)
- **Métodos:**
  - `cadastrar_usuario(usuario: Usuario)`: adiciona um usuário à lista.
  - `registrar_emprestimo(matricula: str, isbn: str)`: valida disponibilidade e limites antes de emprestar.

### **5. Regras de Negócio**

- Um livro só pode ser emprestado se estiver disponível.
- Usuários não podem exceder seu limite de empréstimos.
- Lance exceções personalizadas:
  - `LimiteEmprestimosExcedido`
  - `LivroIndisponivel`

---

## **Tarefa**

Implemente o sistema em Python, criando:

- Classes com encapsulamento adequado (atributos privados, getters/setters se necessário).
- Relacionamentos de herança e polimorfismo.
- Tratamento de exceções para regras de negócio.
- Adicione um método `consultar_livros_emprestados()` na classe `Biblioteca`.

---

## **Dados Iniciais**

### **Tabela de Livros (Acervo da Biblioteca)**

| ISBN   | Título   | Autor   | Disponível? |
| ------ | -------- | ------- | ----------- |
| LIV001 | Titulo 1 | Autor 1 | Sim (True)  |
| LIV002 | Titulo 2 | Autor 2 | Sim (True)  |
| LIV003 | Titulo 3 | Autor 3 | Sim (True)  |
| LIV004 | Titulo 4 | Autor 4 | Sim (True)  |
| LIV005 | Titulo 5 | Autor 5 | Sim (True)  |

### **Tabela de Usuários Cadastrados**

#### **Alunos:**

| Matrícula | Nome   | Tipo  | Livros Emprestados | Limite |
| --------- | ------ | ----- | ------------------ | ------ |
| ALUNOXX1  | Nome 1 | Aluno | []                 | 3      |
| ALUNOXX2  | Nome 2 | Aluno | []                 | 3      |

#### **Professor:**

| Matrícula | Nome      | Tipo      | Livros Emprestados | Limite |
| --------- | --------- | --------- | ------------------ | ------ |
| PROFXX1   | Professor | Professor | []                 | 5      |

---

**Objetivos Avaliados:**  
✔ Abstração e Encapsulamento  
✔ Herança e Polimorfismo  
✔ Tratamento de Exceções  
✔ Modelagem de Classes e Relacionamentos

Boa prova! 📚💻
