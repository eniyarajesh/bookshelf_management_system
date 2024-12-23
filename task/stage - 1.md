# Tasks - CRUD Operations for Library Management System

Below is a comprehensive set of CRUD endpoints for managing books, users, reviews, and categories in a library system using a RESTful API approach. Each task details the corresponding HTTP methods (Create, Read, Update, Delete) along with example JSON requests and responses.

---

## Books API (CRUD Operations)

---

### 1. **Create** (Add a New Book)

#### Request
```json
POST /books
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "1234567890123",
  "publisher": "Charles Scribner's Sons",
  "year_published": 1925,
  "copies_available": 5
}
```

#### Response
```json
{
  "status": "success",
  "message": "Book added successfully",
  "id": "6769be7156ca61f944fa3f90"
}
```

### 2. **Read** (List All Books)

#### Request
```json
GET /books
```

#### Response
```json
{
  "status": "success",
  "data": [
    {
      "id": "6769be7156ca61f944fa3f90",
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "isbn": "1234567890123",
      "publisher": "Charles Scribner's Sons",
      "year_published": 1925,
      "copies_available": 5
    }
  ],
  "total_books": 1
}
```

### 3. **Update** (Update Book Information)

#### Request
```json
PUT /books/6769be7156ca61f944fa3f90
{
  "new_copies_available": 8
}
```

#### Response
```json
{
  "status": "success",
  "message": "Book updated successfully"
}
```

### 4. **Delete** (Delete a Book)

#### Request
```json
DELETE /books/6769be7156ca61f944fa3f90
```

#### Response
```json
{
  "status": "success",
  "message": "Book deleted successfully"
}
```

## Users API (CRUD Operations)

### 1. **Create** (Register a New User)

#### Request
```json
POST /users
{
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "password": "securepassword123"
}
```

#### Response
```json
{
  "status": "success",
  "message": "User registered successfully",
  "id": "6769be7156ca61f944fa3f90"
}
```

### 2. **Read** (Get User Details)

#### Request
```json
GET /users/6769be7156ca61f944fa3f90
```

#### Response
```json
{
  "status": "success",
  "data": {
    "id": "6769be7156ca61f944fa3f90",
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe"
  }
}
```

### 3. **Update** (Update User Information)

#### Request
```json
PUT /users/6769be7156ca61f944fa3f90
{
  "new_email": "new_john@example.com"
}
```

#### Response
```json
{
  "status": "success",
  "message": "User updated successfully"
}
```

### 4. **Delete** (Delete a User)

#### Request
```json
DELETE /users/6769be7156ca61f944fa3f90
```

#### Response
```json
{
  "status": "success",
  "message": "User deleted successfully"
}
```

## Reviews API (CRUD Operations)

### 1. **Create** (Add a Review for a Book)

#### Request
```json
POST /books/6769be7156ca61f944fa3f90/reviews
{
  "content": "A captivating story with deep symbolism.",
  "rating": 5
}
```

#### Response
```json
{
  "status": "success",
  "message": "Review added successfully",
  "id": "6769be7156ca61f944fa3f90"
}
```

### 2. **Read** (List All Reviews for a Book)

#### Request
```json
GET /books/6769be7156ca61f944fa3f90/reviews
```

#### Response
```json
{
  "status": "success",
  "data": [
    {
      "id": "6769be7156ca61f944fa3f90",
      "content": "A captivating story with deep symbolism.",
      "rating": 5
    }
  ]
}
```

### 3. **Update** (Update Review)

#### Request
```json
PUT /books/6769be7156ca61f944fa3f90/reviews/6769be7156ca61f944fa3f90
{
  "content": "An exceptional novel with rich storytelling."
}
```

#### Response
```json
{
  "status": "success",
  "message": "Review updated successfully"
}
```

### 4. **Delete** (Delete a Review)

#### Request
```json
DELETE /books/6769be7156ca61f944fa3f90/reviews/6769be7156ca61f944fa3f90
```

#### Response
```json
{
  "status": "success",
  "message": "Review deleted successfully"
}
```

## Categories API (CRUD Operations)

### 1. **Create** (Add a New Category)

#### Request
```json
POST /categories
{
  "name": "Fiction"
}
```

#### Response
```json
{
  "status": "success",
  "message": "Category created successfully",
  "id": "6769be7156ca61f944fa3f90"
}
```

### 2. **Read** (List All Categories)

#### Request
```json
GET /categories
```

#### Response
```json
{
  "status": "success",
  "data": [
    {
      "id": "6769be7156ca61f944fa3f90",
      "name": "Fiction"
    }
  ]
}
```

### 3. **Update** (Update Category)

#### Request
```json
PUT /categories/6769be7156ca61f944fa3f90
{
  "name": "Historical Fiction"
}
```

#### Response
```json
{
  "status": "success",
  "message": "Category updated successfully"
}
```

### 4. **Delete** (Delete a Category)

#### Request
```json
DELETE /categories/6769be7156ca61f944fa3f90
```

#### Response
```json
{
  "status": "success",
  "message": "Category deleted successfully"
}
```
