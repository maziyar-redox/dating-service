from fastapi import FastAPI

from api.routes.QuestionList import QUESTION_LIST_ROUTE

app = FastAPI()

app.include_router(QUESTION_LIST_ROUTE)

@app.get(
    path="/"
)
def helloWorld():
    return "OK"