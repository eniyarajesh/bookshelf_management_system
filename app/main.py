from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.routes.books import router as book_router
from app.routes.users import router as user_router
from app.routes.reviews import router as review_router
from app.routes.categories import router as category_router

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    for error in exc.errors():
        if error['loc'][-1] == 'isbn':
            return JSONResponse(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                content={"detail": "ISBN must be exactly 13 digits."}
            )
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Validation error occurred."}
    )

app.include_router(book_router)
app.include_router(user_router)
app.include_router(review_router)
app.include_router(category_router)