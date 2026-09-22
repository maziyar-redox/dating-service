from fastapi import APIRouter, status

from enum import Enum

from schema.response.QuestionListPlaceSchema import QuestionListPlaceSchema
from schema.response.QuestionListFoodSchema import QuestionListFoodSchema

from core.RouteTagEnum import RouteTagEnum
from core.ConstantObjects import placesQuestionList
from core.ConstantObjects import foodsQuestionList

TAG: list[str | Enum] | None = [RouteTagEnum.question_list]

QUESTION_LIST_ROUTE = APIRouter(prefix="/question-list", tags=TAG)

@QUESTION_LIST_ROUTE.get(
    path="/places",
    status_code=status.HTTP_200_OK,
    response_model=QuestionListPlaceSchema,
    tags=TAG,
    name="Question List Route(PLACES)",
    description="This route returns all of the questions with their specific id for selection",
    response_description="Successful response"
)
def returnPlacesQuestionListGet() -> QuestionListPlaceSchema:
    return QuestionListPlaceSchema(totalCount=len(placesQuestionList[0].question_list), questions=placesQuestionList)

@QUESTION_LIST_ROUTE.get(
    path="/foods",
    status_code=status.HTTP_200_OK,
    response_model=QuestionListFoodSchema,
    tags=TAG,
    name="Question List Route(FOOD)",
    description="This route returns all of the questions with their specific id for selection",
    response_description="Successful response"
)
def returnFoodsQuestionListGet() -> QuestionListFoodSchema:
    return QuestionListFoodSchema(totalCount=len(foodsQuestionList[0].question_list), questions=foodsQuestionList)