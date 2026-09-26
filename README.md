# MOVE-UP 🚋

Sistema em Python desenvolvido para o desafio proposto pela **SoulUp**, empresa que já opera um sistema de conversão de pontos baseado em economia na conta de luz. Este projeto estende esse modelo para o transporte público: usuários acumulam pontos ao postar conteúdo nas redes sociais e ao economizar energia elétrica, e podem trocar esses pontos por passagens de metrô, trem e ônibus.

> Projeto desenvolvido para a disciplina **Computational Thinking Using Python** (FIAP), em equipe.

---

## 📋 Sobre o projeto

A SoulUp já possui um sistema de conversão de pontos por economia de energia. O desafio proposto aos alunos da FIAP foi estender essa proposta, criando uma solução que também converte pontos ganhos por **engajamento em redes sociais** em **passagens de transporte público**.

A taxa de conversão utilizada é:

> **1 ponto = R$ 0,09**

## ⚙️ Funcionalidades

- **Cadastro e gerenciamento de usuários (CRUD)**, com persistência em `usuarios.json`
- **Acúmulo de pontos** conforme o tipo de postagem (foto, vídeo, story, reels)
- **Conversão de pontos em passagens** de metrô, trem e ônibus
- **Consulta de saldo** e **histórico de transações** do usuário

## 🛠️ Tecnologias utilizadas

- Python 3
- JSON (persistência de dados)

## ▶️ Como executar

```bash
git clone <url-do-repositorio>
cd move-up
python moovup.py
```

> O sistema é executado via menu interativo no terminal.

## 📁 Estrutura do projeto

```
move-up/
├── moovup.py           # Ponto de entrada do sistema (menu principal)
├── usuarios.json      # Base de dados de usuários (persistência local)
└── README.md
```

## 🚀 Próximas melhorias

- [ ] Migração da persistência em JSON para um **banco de dados relacional**
- [ ] Exibição e análise de dados (saldo, histórico, estatísticas de uso) com **pandas**


## 👥 Equipe

| Nome | RM |
|---|---|
| Juan Souza Marques | RM573469 |
| Lucas Leite Carlos | RM571985 |
| Pedro Amaro Pires | RM570636 |
| Matheus Matsushita de Souza | RM570017 |

---

<p align="center">Desenvolvido com 💙 para a disciplina Computational Thinking Using Python — FIAP</p>
