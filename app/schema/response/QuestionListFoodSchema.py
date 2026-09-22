from pydantic import BaseModel

class QuestionListSpecificFoodSchema(BaseModel):
    id: int
    food: str

class QuestionListItemFoodSchema(BaseModel):
    phase: int
    question_list: list[QuestionListSpecificFoodSchema] = []

class QuestionListFoodSchema(BaseModel):
    totalCount: int
    questions: list[QuestionListItemFoodSchema] = []