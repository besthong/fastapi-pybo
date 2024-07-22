import datetime

from typing import List,Union
from pydantic import BaseModel, field_validator
from domain.answer.answer_schema import Answer
from domain.user.user_schema import User

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: List[Answer] = []
    user: Union[User,None]
    modify_date: Union[datetime.datetime,None]
    voter: List[User] = []

class QuestionCreate(BaseModel):
    subject:str
    content:str

    @field_validator('subject','content')
    def not_empty(cls,v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class QuestionList(BaseModel):
    total:int = 0
    question_list: List[Question] = []


class QuestionUpdate(QuestionCreate): #QuestionCreate를 상속함으로써 content, subject를 명세에 포함안해도되고, validator도 작동한다.
    question_id: int

class QuestionDelete(BaseModel):
    question_id: int

class QuestionVote(BaseModel):
    question_id: int
