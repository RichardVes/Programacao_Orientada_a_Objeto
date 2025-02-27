# Conceitos Fundamentais

## 1. Classe

Uma classe é um modelo para criar objetos. Define os atributos e métodos que os objetos daquela classe terão.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
```

## 2. Objeto

Um objeto é uma instância de uma classe.

```python
pessoa1 = Pessoa("Alice", 25)
pessoa1.apresentar()
```

### Exercicios

1. Criando uma Classe Carro
   Crie uma classe chamada Carro com os atributos marca, modelo e ano. Depois, crie um objeto dessa classe e exiba seus atributos.
2. Classe Retângulo com Método para Calcular Área
   Crie uma classe Retangulo que tenha os atributos largura e altura. Adicione um método calcular_area() que retorna a área do retângulo.
3. Criando uma Classe ContaBancaria
   Crie uma classe ContaBancaria com um atributo saldo. Adicione métodos depositar(valor) e sacar(valor), garantindo que o saldo nunca fique negativo.
4. Criando uma Classe Aluno com Nota Final
   Crie uma classe Aluno com os atributos nome e nota. Adicione um método verificar_aprovacao() que retorna "Aprovado" se a nota for maior ou igual a 7, caso contrário, "Reprovado".
5. Criando uma Classe Funcionario com Aumento de Salário
   Crie uma classe Funcionario com os atributos nome e salario. Adicione um método aumentar_salario(percentual) que aumenta o salário conforme o percentual informado.
6. Criando uma Classe Livro
   Crie uma classe chamada Livro com os atributos titulo e autor. Adicione um método detalhes() que exiba as informações do livro.
7. Criando uma Classe Cachorro com Método latir
   Crie uma classe Cachorro com o atributo nome. Adicione um método latir() que exiba "Au Au!" quando chamado.
8. Criando uma Classe Relógio para Mostrar Horário
   Crie uma classe Relogio com os atributos hora, minuto e segundo. Adicione um método mostrar_horario() que exibe o horário formatado.
9. Criando uma Classe Produto com Preço com Desconto
   Crie uma classe Produto com os atributos nome e preco. Adicione um método aplicar_desconto(percentual) que reduz o preço com base no percentual informado.
10. Criando uma Classe Pessoa com um Método de Aniversário
    Crie uma classe Pessoa com os atributos nome e idade. Adicione um método fazer_aniversario() que aumenta a idade da pessoa em 1 ano.

Desafio: Gerenciador de Tarefas
Crie um sistema de Gerenciador de Tarefas utilizando somente classes e objetos. O sistema deve permitir:

Criar tarefas com descrição e status (pendente ou concluída).
Alterar o status da tarefa (de pendente para concluída).
Listar todas as tarefas e indicar quais já foram concluídas.
Regras:

O código deve usar apenas classes e objetos
O usuário pode criar até três tarefas.
As tarefas devem ser exibidas de maneira organizada.
