from pydantic import BaseModel

class QuestionListSpecificPlaceSchema(BaseModel):
    id: int
    text: str

class QuestionListItemPlaceSchema(BaseModel):
    phase: int
    question_list: list[QuestionListSpecificPlaceSchema] = []

class QuestionListPlaceSchema(BaseModel):
    totalCount: int
    questions: list[QuestionListItemPlaceSchema] = []