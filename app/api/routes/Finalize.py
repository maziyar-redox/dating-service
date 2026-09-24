from fastapi import APIRouter, status

from enum import Enum

from datetime import date, datetime

from core.RouteTagEnum import RouteTagEnum
from core.ConstantObjects import placesQuestionList

from utils.searchConstants import SearchPlacesAndFoodsArray

from schema.request.FinalizeListSchema import FinalizeListRequestSchema
from schema.response.FinalizeListSchema import FinalizeListResponseSchema

TAG: list[str | Enum] | None = [RouteTagEnum.finalize_list]

FINALIZE_LIST_ROUTE = APIRouter(prefix="/finalize-list", tags=TAG)

@FINALIZE_LIST_ROUTE.post(
    path="/set",
    status_code=status.HTTP_200_OK,
    response_model=FinalizeListResponseSchema,
    tags=TAG,
    name="Finalize List Route(FOOD)",
    description="This route returns status of accepted request",
    response_description="Successful response"
)
def setFinalizeDatePost(dt: FinalizeListRequestSchema):
    global GLOBAL_VAL
    isAccept = SearchPlacesAndFoodsArray(dt.phase_one, dt.phase_two)
    if isAccept == True:
        GLOBAL_VAL = dt
        return FinalizeListResponseSchema(status=True, date=date.today())
    else:
        GLOBAL_VAL = None
        return FinalizeListResponseSchema(status=False, date=date.today())

@FINALIZE_LIST_ROUTE.get(
    path="/get",
    status_code=status.HTTP_200_OK,
    tags=TAG,
    name="Finalize List Route(FOOD)",
    description="This route returns status of accepted request",
    response_description="Successful response"
)
def getFinalizeDatePost():
    if GLOBAL_VAL == None:
        return False
    else:
        return GLOBAL_VAL