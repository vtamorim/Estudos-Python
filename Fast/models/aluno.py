from pydantic import BaseModel
class Aluno(BaseModel):
    nome : str
    curso : str
    matricula : str
    idade : int
    aprovado : bool | None = None