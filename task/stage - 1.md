# 
# Library Management System - CRUD API Documentation

## Books API (CRUD Operations)

### 1. Create (Add a New Book)
**Request**  
`POST /books`  

**Request Body**  
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "1234567890123",
  "publisher": "Charles Scribner's Sons",
  "year_published": 1925,
  "copies_available": 5
}
```

**Response**  
`201 Created`  
```json
{
  "id": "6769be7156ca61f944fa3f90",
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "1234567890123",
  "publisher": "Charles Scribner's Sons",
  "year_published": 1925,
  "copies_available": 5
}
```

### 2. Read (List All Books)
**Request**  
`GET /books`  

**Response**  
`200 OK`  
```json
[
  {
    "id": "6769be7156ca61f944fa3f90",
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "isbn": "1234567890123",
    "publisher": "Charles Scribner's Sons",
    "year_published": 1925,
    "copies_available": 5
  }
]
```

### 3. Update (Update Book Information)
**Request**  
`PUT /books/6769be7156ca61f944fa3f90`  

**Request Body**  
```json
{
  "copies_available": 8
}
```

**Response**  
`200 OK`  
```json
{
  "id": "6769be7156ca61f944fa3f90",
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "1234567890123",
  "publisher": "Charles Scribner's Sons",
  "year_published": 1925,
  "copies_available": 8
}
```

### 4. Delete (Delete a Book)
**Request**  
`DELETE /books/6769be7156ca61f944fa3f90`  

**Response**  
`204 No Content`  

---

## Users API (CRUD Operations)

### 1. Create (Register a New User)
**Request**  
`POST /users`  

**Request Body**  
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "password": "securepassword123"
}
```

**Response**  
`201 Created`  
```json
{
  "id": "6769be7156ca61f944fa3f90",
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe"
}
```

### 2. Read (Get User Details)
**Request**  
`GET /users/6769be7156ca61f944fa3f90`  

**Response**  
`200 OK`  
```json
{
  "id": "6769be7156ca61f944fa3f90",
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe"
}
```

### 3. Update (Update User Information)
**Request**  
`PUT /users/6769be7156ca61f944fa3f90`  

**Request Body**  
```json
{
  "email": "new_john@example.com"
}
```

**Response**  
`200 OK`  
```json
{
  "id": "6769be7156ca61f944fa3f90",
  "username": "john_doe",
  "email": "new_john@example.com",
  "full_name": "John Doe"
}
```

### 4. Delete (Delete a User)
**Request**  
`DELETE /users/6769be7156ca61f944fa3f90`  

**Response**  
`204 No Content`  

---

## Reviews API (CRUD Operations)

### 1. Create (Add a Review for a Book)
**Request**  
`POST /books/6769be7156ca61f944fa3f90/reviews`  

**Request Body**  
```json
{
  "content": "A captivating story with deep symbolism.",
  "rating": 5
}
```

**Response**  
`201 Created`  
```json
{
  "id": "9876fd7156ca61f944fa3f91",
  "book_id": "6769be7156ca61f944fa3f90",
  "content": "A captivating story with deep symbolism.",
  "rating": 5
}
```

### 2. Read (List All Reviews for a Book)
**Request**  
`GET /books/6769be7156ca61f944fa3f90/reviews`  

**Response**  
`200 OK`  
```json
[
  {
    "id": "9876fd7156ca61f944fa3f91",
    "book_id": "6769be7156ca61f944fa3f90",
    "content": "A captivating story with deep symbolism.",
    "rating": 5
  }
]
```

### 3. Update (Update Review)
**Request**  
`PUT /books/6769be7156ca61f944fa3f90/reviews/9876fd7156ca61f944fa3f91`  

**Response**  
`200 OK`  
```json
{
  "id": "9876fd7156ca61f944fa3f91",
  "book_id": "6769be7156ca61f944fa3f90",
  "content": "An exceptional novel with rich storytelling.",
  "rating": 5
}
```

### 4. Delete (Delete a Review)
**Request**  
`DELETE /books/6769be7156ca61f944fa3f90/reviews/9876fd7156ca61f944fa3f91`  

**Response**  
`204 No Content`


## Categories API (CRUD Operations)

### 1. Create (Add a New Category)
**Request**  
`POST /categories`  

**Request Body**  
```json
{
  "name": "Fiction"
}
```

**Response**  
`201 Created`  
```json
{
  "id": "6769be7156ca61f944fa3f90",
  "name": "Fiction"
}
```

---

### 2. Read (List All Categories)
**Request**  
`GET /categories`  

**Response**  
`200 OK`  
```json
[
  {
    "id": "6769be7156ca61f944fa3f90",
    "name": "Fiction"
  }
]
```

---

### 3. Update (Update Category)
**Request**  
`PUT /categories/6769be7156ca61f944fa3f90`  

**Request Body**  
```json
{
  "name": "Historical Fiction"
}
```

**Response**  
`200 OK`  
```json
{
  "id": "6769be7156ca61f944fa3f90",
  "name": "Historical Fiction"
}
```

---

### 4. Delete (Delete a Category)
**Request**  
`DELETE /categories/6769be7156ca61f944fa3f90`  

**Response**  
`204 No Content`  

