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

---
