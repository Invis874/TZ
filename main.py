from fastapi import Depends, FastAPI, HTTPException
#from sqlalchemy.orm import Session

from sql_app import models
from sql_app.database import Session, engine

import requests

models.Base.metadata.create_all(bind=engine)
Questions= models.Questions

app = FastAPI()

@app.get("/")
def read_root(integer: int):
    return integer


@app.post("/")
def post_root(integer: int):
    questions(integer)

    return integer

def questions(n):
    response = requests.get(f'https://jservice.io/api/random?count={n}').json()
    i = 0
    answer = None
    x = []
    while i < n:
        session = Session()
        if session.query(Questions.id_question).filter(Questions.id_question == response[i]["id"]) != response[i]["id"]:
            id_question = response[i]["id"]
            question = response[i]["question"]
            if len(session.query(Questions).all()) > 0:
                answer = session.query(Questions.question).filter(Questions.id == len(session.query(Questions).all()))
            else:
                pass
            creation_date = response[i]["airdate"]

            question = Questions(id_question=id_question, question=question,
                                 answer=answer, creation_date=creation_date)

            session.add(question)
            session.commit()
            x.append([id_question, question, answer,  creation_date])
        else:
            session.commit()
            questions(i)
            return x
        i += 1

    return x