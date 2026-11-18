# 📘 Atividade: Persistência de Dados com SQLite

## 🎯 Objetivo

Crie um gerenciador simples de notas em Python que armazene dados em um banco SQLite e os mantenha disponíveis entre execuções. Pratique criação de tabelas e operações CRUD usando consultas SQL parametrizadas.

## 📝 Tarefas

### 🛠️ Criar o banco de dados e a tabela

#### Descrição

Complete `initialize_database()` no arquivo `starter-code.py` para criar o banco de dados e uma tabela para armazenar notas.

#### Requisitos

O programa concluído deve:

- Criar o arquivo `notes.db` na pasta da atividade ao conectar-se ao banco.
- Criar uma tabela `notes` com as colunas `id`, `title` e `content`.
- Usar `id` como chave primária e exigir valores para `title` e `content`.
- Poder executar a inicialização mais de uma vez sem causar erro se a tabela já existir.

### 🛠️ Adicionar e consultar notas

#### Descrição

Implemente as funções para inserir notas no banco de dados e consultar todas as notas cadastradas.

#### Requisitos

O programa concluído deve:

- Inserir o título e o conteúdo de uma nota e retornar o identificador gerado pelo banco.
- Listar as notas com seus identificadores, títulos e conteúdos, em ordem crescente de identificador.
- Usar parâmetros `?` nas consultas SQL para fornecer os valores inseridos.

Exemplo de uso:

```python
initialize_database()
note_id = add_note("Revisar SQLite", "Praticar consultas")
print(list_notes())
```

### 🛠️ Atualizar e excluir notas

#### Descrição

Implemente as funções para atualizar e remover uma nota existente, identificada pelo seu `id`.

#### Requisitos

O programa concluído deve:

- Atualizar o título e o conteúdo da nota indicada e retornar `True` se uma linha foi alterada ou `False` se o identificador não existir.
- Excluir a nota indicada e retornar `True` se uma linha foi removida ou `False` se o identificador não existir.
- Manter as alterações no banco para que as notas continuem disponíveis após encerrar e executar o programa novamente.
