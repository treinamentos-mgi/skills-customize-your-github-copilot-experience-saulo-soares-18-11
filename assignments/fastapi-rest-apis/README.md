# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Crie uma API REST em Python usando FastAPI para gerenciar uma lista de tarefas. Você vai praticar rotas HTTP, validação de dados com modelos e operações CRUD com respostas e códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Consultar tarefas pela API

#### Descrição

Use o arquivo `starter-code.py` como ponto de partida. Instale as dependências com `pip install fastapi uvicorn` e execute a aplicação com `uvicorn starter-code:app --reload`. Implemente as rotas para consultar todas as tarefas e consultar uma tarefa pelo identificador.

#### Requisitos

O programa concluído deve:

- Responder a `GET /tasks` com a lista de tarefas em memória.
- Responder a `GET /tasks/{task_id}` com a tarefa correspondente.
- Retornar o status HTTP `404` quando o identificador não corresponder a uma tarefa.

### 🛠️ Criar tarefas com validação

#### Descrição

Implemente a rota para criar tarefas. Use o modelo Pydantic fornecido no código inicial para validar os dados recebidos no corpo da requisição.

#### Requisitos

O programa concluído deve:

- Aceitar requisições `POST /tasks` com um título e, opcionalmente, o estado de conclusão.
- Gerar um identificador único para cada nova tarefa e adicioná-la à lista em memória.
- Retornar a tarefa criada com status HTTP `201`.
- Rejeitar dados inválidos usando a validação do modelo Pydantic.

Exemplo de corpo da requisição:

```json
{
  "title": "Estudar FastAPI",
  "completed": false
}
```

### 🛠️ Atualizar e excluir tarefas

#### Descrição

Implemente as rotas para atualizar uma tarefa existente e removê-la da lista.

#### Requisitos

O programa concluído deve:

- Aceitar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão da tarefa.
- Aceitar `DELETE /tasks/{task_id}` para remover a tarefa e retornar o status HTTP `204`.
- Retornar o status HTTP `404` ao tentar atualizar ou excluir uma tarefa inexistente.
