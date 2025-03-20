# Aula 4 - Herança em Python

## Introdução

A herança é um dos pilares da Programação Orientada a Objetos (POO) e permite que uma classe (subclasse) herde atributos e métodos de outra classe (superclasse). Isso promove reutilização de código e facilita a manutenção.

---

## 1. Conceitos

### O que é Herança?

Herança é o mecanismo que permite a criação de novas classes a partir de classes existentes, aproveitando e especializando comportamentos já definidos. A classe que herda é chamada de **subclasse**, e a classe base é chamada de **superclasse**.

**Vantagens da herança:**

- Reutilização de código.
- Facilidade de manutenção.
- Melhor organização do código.

---

## 2. Exemplo de Herança em Python

### Criando a Superclasse

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."
```

### Criando a Subclasse

```python
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # Chamada ao construtor da superclasse
        self.curso = curso

    def apresentar(self):
        return f"Meu nome é {self.nome}, tenho {self.idade} anos e estudo {self.curso}."
```

### Usando as Classes

```python
pessoa = Pessoa("Carlos", 40)
print(pessoa.apresentar())  # Meu nome é Carlos e tenho 40 anos.

estudante = Estudante("Ana", 20, "Engenharia")
print(estudante.apresentar())  # Meu nome é Ana, tenho 20 anos e estudo Engenharia.
```

---

## 3. Tipos de Herança

### 3.1. Herança Simples

Uma classe herda diretamente de uma outra classe.

```python
class Animal:
    def emitir_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"
```

### 3.2. Herança Múltipla

Uma classe pode herdar de múltiplas classes.

```python
class Mamifero:
    def caracteristica(self):
        return "Amamenta os filhotes"

class Ave:
    def caracteristica(self):
        return "Tem penas"

class Morcego(Mamifero, Ave):
    pass

morcego = Morcego()
print(morcego.caracteristica())  # Amamenta os filhotes
```

### 3.3. Herança Multinível

Uma classe herda de outra, que já herdou de uma terceira classe.

```python
class Veiculo:
    def tipo(self):
        return "Veículo"

class Carro(Veiculo):
    def rodas(self):
        return 4

class Esportivo(Carro):
    def velocidade_maxima(self):
        return 300
```

---

## 4. Exercícios

### Exercício 1: Criando uma Hierarquia de Veículos

**Crie uma classe **Veiculo** com os atributos `marca` e `ano`. Em seguida, crie as subclasses **Carro** e **Moto**, que herdam de `Veiculo`. Ambas devem ter um método `info()` que exibe as informações do veículo.
**

### Exercício 2: Herança Multinível

Crie uma classe **Funcionario** com os atributos `nome` e `salario`. Depois, crie uma subclasse **Gerente**, que adiciona um atributo `departamento`. Por fim, crie uma subclasse **Diretor**, que tem um atributo `bonus`.

### Exercício 3: Reescrevendo Métodos

**Crie uma classe **InstrumentoMusical** com um método `tocar()`. Depois, crie as subclasses **Guitarra** e **Bateria**, sobrescrevendo o método `tocar()` para exibir uma mensagem diferente para cada instrumento.
**
---\*\*\*\*
