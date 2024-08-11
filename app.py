# Import the Flask framework for creating web applications and
# Flask-SQLAlchemy for database interactions
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 

# Create a Flask application instance
app = Flask(__name__)  

# Configure the database URI (replace with your PostgreSQL credentials)
# This line specifies the connection string to your PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pass@localhost:5432/bookstore'

# This line disables tracking modifications, improving performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy instance for database management
db = SQLAlchemy(app)  

# Define the Book model (a blueprint for book data)
class Book(db.Model):  # Inherit from db.Model to create a database table
    id = db.Column(db.Integer, primary_key=True)  # Define an integer column for the book ID, set as primary key
    title = db.Column(db.String(120), nullable=False)  # Define a string column for the book title, cannot be null
    author = db.Column(db.String(80), nullable=False)  # Define a string column for the book author, cannot be null

    def to_dict(self):  # Define a method to convert Book instance to a dictionary
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
        }
    
    def __repr__(self):  # Define a string representation of a book instance for debugging
        return f'<Book {self.id} - {self.title}>'

# API Endpoints

# hello world of books
@app.route('/')
def hello():
    return('Hello there you book lover, try this to check you app..http://127.0.0.1:5000/books')

# Create book 
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    book = Book(title=data['title'], author=data['author'])
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully', 'book': book.to_dict()}), 201


# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# Get a specific book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book.title = data['title']
    book.author = data['author']
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})


# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})


if __name__ == '__main__':  # Run the Flask app if this script is executed directly
    app.run(debug=True)  # Start the development server with debugging enabled
