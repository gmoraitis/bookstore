## Book Manager App

A simple fullstack app - exercise to guide me throught the process of adding an authendication setup procedure with `Keycloack`.

### Procedure - Notes - To-do

#### 1. Project Setup and Backend Development
- Create a new Python project directory and set up a virtual environment to isolate project dependencies.
- Inside the project folder
```bash
python -m venv venv
```
- Activate the virual Enviroment
```bash
source venv/bin/activate
```

- Install Flask and database library.
    -   #### ! Which database ? Knowlegde here:
        - `PostgreSQL` is a robust, open-source relational database system known for its reliability, performance, and feature-richness. It's an excellent choice for our book manager application.

        - `Flask-SQLAlchemy` is an extension for Flask that provides an ORM (Object-Relational Mapper) interface for interacting with databases. It simplifies database operations, making it easier to work with PostgreSQL in our Flask app.

        - Why This Combination?
        PostgreSQL offers a solid foundation for our data storage needs, providing features like transactions, foreign keys, and indexing.
        Flask-SQLAlchemy streamlines database interactions, allowing us to define models as Python classes and perform CRUD operations without writing raw SQL.
        
        - By using this combination, we'll benefit from:
        - Improved productivity: Flask-SQLAlchemy simplifies database interactions.
        - Enhanced data integrity: PostgreSQL ensures data consistency and reliability.
        - Scalability: PostgreSQL can handle increasing data volumes and concurrent users.
- Define database models for books (title, author, etc.).
- Create Flask app with routes for book CRUD operations (create, read, update, delete).
- Implement database interactions using PostgreSQL and Flask-SQLAlchemy.

```bash
pip install Flask Flask-SQLAlchemy psycopg2
```
This will install:

Flask: The web framework for our application.
Flask-SQLAlchemy: For database interactions.
psycopg2: The PostgreSQL adapter for Python.


##### Building the Flask app and defining the database model.
- We need to :
    - Import Flask and Flask-SQLAlchemy.
    - Create a Flask application instance.
    - Configure the database URI with your PostgreSQL credentials.
    - Create a SQLAlchemy instance.
    - Define the Book model with columns for id, title, and author.
    - ! First create a table from the Postgresql command line and then use the API(app.py) !
    - ? Do we need  def to_dict(self): method ?
    - (is obligatory ? )The __repr__ method provides a string representation of a book instance for debugging purposes.

Added procedure:
run the local database
```bash
sudo -u postgres psql -d bookstore
```
run the app.py
```bash
python3 app.py
```
make requests with curl
```bash
# create books
curl -X POST -H "Content-Type: application/json" -d '{
"title": "The book of my life", "author": "john Doe"}' http://127.0.0.1:5000/books

# get books or a spesific book
curl http://127.0.0.1:5000/books
curl http://127.0.0.1:5000/books/<id>

# update book
curl -X POST -H "Content-Type: application/json" -d '{
"title": "The book of my life", "author": "john Doe"}' http://127.0.0.1:5000/books

# delete a book
curl -X DELETE http://127.0.0.1:5000/books/<id>




#### 2. Frontend Development with React
- Create a new React project using Vite.
- Design UI components for book listing, book form, and user interface (simple design for the meaning of the project).
- Implement state management for book data using React Context or Redux (not in the beginning!).
- Fetch book data from backend using API calls.
- Handle form submissions to create, update, and delete books.
#### 3. Integration and Testing
- Connect frontend to backend using API calls.
- Thoroughly test both frontend and backend functionalities (...later).
- Implement error handling for API requests and database operations(...later).
#### 4. Authentication with Keycloak ( -->> main learning subject here..add more notes)
- Integrate Keycloak into the backend.
- Implement token-based authentication for protected routes.
- Secure API endpoints with authentication checks.
- Handle user authorization based on roles or permissions (if needed).
#### 5. Dockerization (...Later but needs study here !)
- Create Dockerfiles for both frontend and backend.
- Define Docker Compose for multi-container setup (for database, frontend, and backend).
- Build and run Docker images to deploy the application.



## Linux commands used so far...
- `mkdir`: to create the directory of the project
- `cd [bookstore]` : to move to the new directory
- `touch [README.md]` : to create a new file,  and also the same for gitignore
- `rm -r [virtualenv]` : to delete a wrongly setup of venv folder

 