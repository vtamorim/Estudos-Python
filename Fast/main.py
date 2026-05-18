from fastapi import FastAPI
from pydantic import BaseModel
from routes.item_routes import router
app = FastAPI()
app.include_router(router)
class Aluno(BaseModel):
    
    nome : str
    curso : str
    matricula : str
    idade : int
    aprovado : bool | None = None


@app.get("/")
async def read_root():
    return [{"Nome": "Victor Miguel", "Curso": "Informática para Internet", "Matrícula" : "20241011110003", "Idade" : 17, "Aprovado" : None}
    ,{"Nome" : "Sla que", "Curso" : "sla tbm", "Matricula" : "hm", "Idade": 0, "Aprovado" : None}
    ]

@app.get("/alunos/{aluno_id}")
async def read_aluno(aluno_id: int, q: str | None = None):
    return {"aluno_id": aluno_id, "q": q}

@app.put("/alunos/{aluno_id}")
async def update_aluno(aluno_id : int, aluno : Aluno):
    return {"aluno_nome" : aluno.nome, "aluno_id": aluno_id}