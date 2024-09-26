# app.py

# Import necessary modules and packages
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Initialize the Flask application
app = Flask(__name__)

# Configure the application settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neurobudget.db'  # Database URI
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Secret key for JWT

# Initialize extensions
db = SQLAlchemy(app)  # Initialize SQLAlchemy for ORM
bcrypt = Bcrypt(app)  # Initialize Bcrypt for password hashing
jwt = JWTManager(app)  # Initialize JWT manager for authentication

# Define routes (add your route imports here)
from routes.auth import *
from routes.budget import *

# A simple test route to check if the backend is running
@app.route('/')
def index():
    return jsonify({"message": "Welcome to NeuroBudget Backend!"})

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
