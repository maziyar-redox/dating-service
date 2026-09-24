from fastapi import FastAPI

from api.routes.QuestionList import QUESTION_LIST_ROUTE
from api.routes.Finalize import FINALIZE_LIST_ROUTE

app = FastAPI()

app.include_router(QUESTION_LIST_ROUTE)
app.include_router(FINALIZE_LIST_ROUTE)

@app.get(
    path="/health"
)
def helloWorld():
    return "OK"