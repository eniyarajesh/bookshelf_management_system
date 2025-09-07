from bson.objectid import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import HTTPException, status
from datetime import datetime
from app2.models.book import Book
from app2.schemas.book import CreateBook, UpdateBook, ResponseBook, PublisherInfo
from app2.services import BaseService


class BookService(BaseService):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['books']
        self.collection = db['publisher']

    async def _enrich_publisher(self, publisher_ids):
        """ Helper to fetch publisher details from ID(s) """
        if not publisher_ids:
            return None
        if isinstance(publisher_ids, list) and len(publisher_ids) > 0:
            pub_id = publisher_ids[0]
        else:
            pub_id = publisher_ids

        pub = await self.publisher_collection.find_one({"_id": ObjectId(pub_id)})
        if pub:
            return PublisherInfo(id=str(pub["_id"]), name=pub["name"])
        return None

    async def get_books(self):
        results = await self.collection.find().to_list(None)
        books = []
        for book in results:
            enriched_publisher = await self._enrich_publisher(book.get("publisher", []))
            books.append(ResponseBook(
                id=str(book["_id"]),
                name=book.get("name"),
                description=book.get("description"),
                created_at=book.get("created_at").isoformat() if book.get("created_at") else None,
                updated_at=book.get("updated_at").isoformat() if book.get("updated_at") else None,
                average_rating=book.get("average_rating"),
                total_reviews=book.get("total_reviews"),
                is_published=book.get("is_published", False),
                publisher=enriched_publisher
            ))
            # books.append(self._to_response(res, ResponseBook))
        return books

    async def create_book(self, book_data: CreateBook):
        book_dict = book_data.model_dump()
        book_dict["_id"] = str(ObjectId())
        book_dict["created_at"] = book_dict["updated_at"] = datetime.utcnow()
        # book_dict["_id"] = str(ObjectId())
        book_dict["total_reviews"] = 10
        result = await self.collection.insert_one(book_dict)
        book = await self.collection.find_one({'_id': result.inserted_id})
        # existing_book = await self.collection.find_one({'_id': book_dict['isbn']})
        # if existing_book:
        #     raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail=f"Book with ISBN {book_dict['isbn']} already exists" )
        return self._to_response(book, ResponseBook)
    
    async def get_book(self, book_id: str):
        try:
            result = await self.collection.find_one({'_id': book_id})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        # return self._to_response(result, ResponseBook)
        enriched_publisher = await self._enrich_publisher(result.get("publisher", []))

        return ResponseBook(
            id=str(result["_id"]),
            name=result.get("name"),
            description=result.get("description"),
            created_at=result.get("created_at").isoformat() if result.get("created_at") else None,
            updated_at=result.get("updated_at").isoformat() if result.get("updated_at") else None,
            average_rating=result.get("average_rating"),
            total_reviews=result.get("total_reviews"),
            is_published=result.get("is_published", False),
            publisher=enriched_publisher
        )
    

    async def update_books(self, book_id: str, update_data: UpdateBook):
        try:
            result = await self.collection.update_one({'_id': book_id},
                                                      {'$set': update_data.dict(exclude_unset=True)})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        result = await self.collection.find_one({'_id': book_id})
        return self._to_response(result, ResponseBook)


    async def delete_book(self, book_id: str):
        try:
            result = await self.collection.delete_one({'_id': book_id})
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        return {f"{book_id} is sussussfully deleted"}
    