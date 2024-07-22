import datetime
from typing import Union,List
from pydantic import BaseModel, field_validator
from domain.user.user_schema import User

class AnswerCreate(BaseModel):
    content: str

    @field_validator('content')
    def not_empty(cls,v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v


class Answer(BaseModel):
    id: int
    content:str
    create_date: datetime.datetime
    user: Union[User,None]
    question_id: int
    modify_date: Union[datetime.datetime,None]
    voter: List[User] = []

class AnswerUpdate(AnswerCreate): #Question 모델과 동일하게, AnswerCreate을 상속받아 id만 가져오도록 설정
    answer_id: int


class AnswerDelete(BaseModel):
    answer_id : int


class AnswerVote(BaseModel):
    answer_id: int

