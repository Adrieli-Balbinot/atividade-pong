# 🕹️ Pong em Python com Pygame

Este projeto consiste em uma implementação do clássico jogo **Pong**, desenvolvido em Python utilizando a biblioteca `pygame`. O código foi refatorado com foco em boas práticas de desenvolvimento, como **organização, legibilidade e aplicação de princípios de engenharia de software**.

---

## 🚀 Funcionalidades

* 🎮 Controle do jogador (setas ↑ ↓)
* 🤖 Oponente com inteligência artificial simples
* ⚽ Movimentação da bola com colisões
* 🧮 Sistema de pontuação
* 📋 Menu inicial interativo

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Pygame

Instalação do pygame:

```bash
pip install pygame
```

Execução do projeto:

```bash
python pong.py
```

---

## 📂 Estrutura do Código

O projeto foi organizado em classes com responsabilidades bem definidas:

* `Config` → Configurações globais do jogo
* `Raquete` → Representa os jogadores
* `Bola` → Responsável pela lógica da bola
* `Game` → Controla a lógica principal do jogo
* `Menu` → Gerencia a interface inicial
* `main()` → Inicialização do sistema

---

# 🧠 Conceitos Aplicados

## 🔹 Abstração

A abstração foi aplicada na modelagem dos elementos do jogo:

* A classe `Raquete` encapsula comportamento e atributos de uma raquete (movimento e desenho).
* A classe `Bola` abstrai toda a lógica relacionada à bola (movimento, colisões e reset).
* A classe `Game` abstrai o funcionamento completo do jogo.

👉 Isso permite que cada entidade represente claramente um conceito do mundo real.

---

## 🔹 Separação de Responsabilidades

Cada classe possui uma responsabilidade única:

* `Menu` → responsável apenas pela interface inicial
* `Game` → controla o fluxo do jogo
* `Raquete` → controla apenas movimentação e renderização da raquete
* `Bola` → controla apenas a lógica da bola

👉 Isso evita acoplamento excessivo e facilita manutenção.

---

## 🔹 Princípios SOLID

### ✅ S — Single Responsibility Principle (SRP)

Cada classe tem apenas um motivo para mudar:

* `Bola` → apenas lógica da bola
* `Raquete` → apenas comportamento da raquete
* `Menu` → apenas interface inicial

---

### ✅ O — Open/Closed Principle (OCP)

O código está aberto para extensão, mas fechado para modificação:

* É possível adicionar novos comportamentos sem alterar as classes existentes.
* Novos modos de jogo poderiam ser adicionados criando novas classes.

---

### ⚠️ L — Liskov Substitution Principle (LSP)

Não há herança no projeto, então este princípio não se aplica diretamente.
Porém, o design permite futura extensão com herança sem quebrar comportamento esperado.

---

### ⚠️ I — Interface Segregation Principle (ISP)

Não há interfaces formais, mas as classes possuem métodos específicos e enxutos, evitando dependências desnecessárias.

---

### ⚠️ D — Dependency Inversion Principle (DIP)

O projeto ainda depende diretamente do `pygame`, ou seja:

* Não há abstração para camada gráfica
* Poderia ser melhorado criando interfaces para renderização

👉 Esse ponto pode ser evoluído em versões futuras.

---

## 🔹 Legibilidade

O código foi estruturado para facilitar a leitura:

* Uso de nomes claros (`mover_cima`, `verificar_colisoes`)
* Organização em seções:

  * Configurações
  * Entidades
  * Lógica
  * Menu
* Métodos pequenos e objetivos
* Comentários explicativos em cada classe e função

---

## 🔹 Documentação

O código possui documentação interna com **docstrings**, explicando:

* O propósito de cada classe
* O comportamento de cada método

Exemplo:

```python
def mover(self):
    """Atualiza a posição da bola."""
```

👉 Isso facilita entendimento e manutenção do código.

---

## 👩‍💻 Autor

Projeto desenvolvido como atividade acadêmica com foco em **refatoração e boas práticas de programação**.
