# Import the Flask framework for creating web applications and
# Flask-SQLAlchemy for database interactions
from flask import Flask  
from flask_sqlalchemy import SQLAlchemy 

# Create a Flask application instance
app = Flask(__name__)  

# Configure the database URI (replace with your PostgreSQL credentials)
# This line specifies the connection string to your PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_username:your_password@your_host:your_port/your_database_name'
# This line disables tracking modifications, improving performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy instance for database management
db = SQLAlchemy(app)  

# Define the Book model (a blueprint for book data)
class Book(db.Model):  # Inherit from db.Model to create a database table
    id = db.Column(db.Integer, primary_key=True)  # Define an integer column for the book ID, set as primary key
    title = db.Column(db.String(120), nullable=False)  # Define a string column for the book title, cannot be null
    author = db.Column(db.String(80), nullable=False)  # Define a string column for the book author, cannot be null

    def __repr__(self):  # Define a string representation of a book instance for debugging
        return f'<Book {self.id} - {self.title}>'

if __name__ == '__main__':  # Run the Flask app if this script is executed directly
    app.run(debug=True)  # Start the development server with debugging enabled
