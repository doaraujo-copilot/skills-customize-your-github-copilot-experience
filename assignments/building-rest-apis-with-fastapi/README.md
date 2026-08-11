# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API with FastAPI that manages a collection of books and exposes endpoints for reading, creating, updating, and deleting records.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Create a new FastAPI app and define a health check endpoint so the server responds with JSON.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance.
- Add a `GET /health` route that returns a simple JSON response.
- Run the app locally with Uvicorn or the FastAPI development server.

### 🛠️ Build CRUD Endpoints for Books

#### Description
Implement endpoints that allow clients to list books, create a new book, retrieve one book by ID, update an existing book, and delete a book.

#### Requirements
Completed program should:

- Define a `Book` model with fields such as `title`, `author`, and `year`.
- Store books in an in-memory list.
- Implement these routes:
  - `GET /books`
  - `POST /books`
  - `GET /books/{book_id}`
  - `PUT /books/{book_id}`
  - `DELETE /books/{book_id}`
- Return JSON data in a clear and consistent structure.

### 🛠️ Validate Input and Handle Errors

#### Description
Improve your API by validating request data and returning helpful errors when a book is not found.

#### Requirements
Completed program should:

- Use Pydantic validation so invalid input is rejected.
- Ensure required fields are present and values are reasonable.
- Return a `404` response with a clear message when a requested book does not exist.
- Use appropriate status codes for successful create, update, and delete operations.
