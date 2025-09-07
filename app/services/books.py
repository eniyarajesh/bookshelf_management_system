from bson.objectid import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import HTTPException, status
from app.models.books import Book
from app.schemas.books import BookCreate, BookResponse, BookUpdate
from app.services import BaseService


class BookService(BaseService):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['books']

    async def create_book(self, book_data: BookCreate):
        book_dict = book_data.dict()

        existing_book = await self.collection.find_one({'isbn': book_dict['isbn']})
        if existing_book:
            raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail=f"Book with ISBN {book_dict['isbn']} already exists" )

        string_id = str(ObjectId())
        book_dict['_id'] = string_id 
        await self.collection.insert_one(book_dict)
        book = await self.collection.find_one({'_id': string_id})
        return self._to_response(book, BookResponse)

    async def get_book(self, book_id: str):
        try:
            book = await self.collection.find_one({'_id': str(ObjectId(book_id))})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        return self._to_response(book, BookResponse)

    async def update_book(self, book_id: str, update_data: BookUpdate):
        try:
            obj_id = ObjectId(book_id)
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")

        current_book = await self.collection.find_one({'_id': str(obj_id)})
        if not current_book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

        new_isbn = update_data.isbn
        if new_isbn and new_isbn != current_book.get("isbn"):
            duplicate = await self.collection.find_one({
                'isbn': new_isbn,
                '_id': {'$ne': str(obj_id)}
            })
            if duplicate:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Another book with ISBN {new_isbn} already exists"
                )
        result = await self.collection.update_one(
            {'_id': str(obj_id)},
            {'$set': update_data.dict(exclude_unset=True)}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        book = await self.collection.find_one({'_id': str(obj_id)})
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found after update")

        return self._to_response(book, BookResponse)


    async def delete_book(self, book_id: str):
        try:
            result = await self.collection.delete_one({'_id': str(ObjectId(book_id))})
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")

    async def get_books(self):
        books = await self.collection.find().to_list(None)
        return [self._to_response(book, BookResponse) for book in books]
