from sqlmodel import Field, SQLModel,create_engine
from .model import *


sq_lite_file_name = 'databases.db'
sq_lite_url = f'sqlite:///{sq_lite_file_name}'


engine = create_engine(sq_lite_url, echo=True)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine )