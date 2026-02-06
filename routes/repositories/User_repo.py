from models import user
from sqlalchemy.orm import Session

class UserRepo:
    def __init__(self,db:Session):
        self.db=db
    
    def create_user(self,user:user):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user