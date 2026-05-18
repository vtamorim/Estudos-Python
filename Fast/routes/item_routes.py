from fastapi import APIRouter
from models.aluno import Aluno

router = APIRouter(prefix="/alunos", tags=["alunos"])

alunos = []
@router.post("/alunos/{aluno_id}")
async def create_aluno(aluno_id: int, aluno: Aluno):
    pass

@router.get("/alunos")
async def list_alunos():
    pass

@router.get("/alunos/{aluno_id}")
async def get_aluno(aluno_id: int):
    pass