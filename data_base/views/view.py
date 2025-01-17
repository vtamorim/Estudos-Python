import __init__
from model.database import engine
from model.model import Subscribe, Paymodel
from sqlmodel import Session, select
from datetime import date

class Servicesubscribe:
    def __init__(self, engine):
        self.engine = engine
    def create(self, subscription: Subscribe):
        with Session(self.engine) as session:
            session.add(subscribe)
            session.commit()
            return subscribe
    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscribe)
            results = session.exec(statement).all()
        return results
    def pay(self,subcribe:Subscribe):
        with Session(self.engine) as session:
            statement = select(Paymodel).where(Subscribe.empresa ==subcribe.empresa)
            results = session.exec(statement).all()
            print(results)    

x = Servicesubscribe(engine)
#subscribe = Subscribe(empresa='Pythonando', site='pythonando.com.br', data_assinatura= date.today(), valor=37.90)
#x.pay(subscribe)