## Book Manager App

A simple fullstack app - exercise to guide me throught the process of adding an authendication setup procedure with `Keycloack`.

### Procedure - Notes - To-do

#### 1. Project Setup and Backend Development
- Create a new Python project directory and set up a virtual environment to isolate project dependencies.
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
 