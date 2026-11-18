from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Tasks API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool


tasks = [
    {"id": 1, "title": "Estudar FastAPI", "completed": False},
]
next_task_id = 2


@app.get("/tasks")
def list_tasks():
    # TODO: Retorne todas as tarefas.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Encontre e retorne a tarefa ou lance HTTPException com status 404.
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # TODO: Crie um identificador, adicione a tarefa à lista e retorne-a.
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):
    # TODO: Atualize a tarefa ou lance HTTPException com status 404.
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    # TODO: Remova a tarefa ou lance HTTPException com status 404.
    # Em caso de sucesso, retorne Response(status_code=status.HTTP_204_NO_CONTENT).
    pass
