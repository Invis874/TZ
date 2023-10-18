from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    id_question = Column(Integer)
    question = Column(String)
    answer = Column(String)
    creation_date = Column(String)