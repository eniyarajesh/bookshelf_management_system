from fastapi import FastAPI
from app2.routes.publisher import router as publisher_router
from app2.routes.bookstore import router as bookstore_router
from app2.routes.category import router as category_router
from app2.routes.user import router as user_router
from app2.routes.book import router as book_router
from app2.routes.author import router as author_router


app = FastAPI()

app.include_router(publisher_router)
app.include_router(bookstore_router)
app.include_router(category_router)
app.include_router(user_router)
app.include_router(book_router)
app.include_router(author_router)

@app.get("/")
def home():
    return {"message": "Welcome to the API"}