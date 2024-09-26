


Documentation for app.py
What is app.py?
app.py is the main file for your Flask application. Think of it as the control center that starts everything and tells your app how to behave.

Key Parts
Imports:

At the top, we import the tools we need from Flask and other libraries. These tools help us manage the database, hash passwords, and handle user authentication.
Create the App:

app = Flask(__name__): This line creates our Flask app. It's like saying, "Hey, I'm starting my app!"
Configuration:

We set up some basic settings for the app, like where to find our database and the secret key used for user authentication. This key keeps our app secure.
Database Setup:

db = SQLAlchemy(app): This line connects our app to the database. It allows us to store and retrieve data, like user information and transactions.
Define Routes:

We import routes (like /register and /login) from other files. Routes are the paths where users can send requests, such as signing up or logging in.
Test Route:

There’s a simple route (/) that returns a welcome message. This is a way to check that everything is working.
Run the App:

app.run(debug=True): This line starts the app. The debug=True part means that if we make a mistake in our code, we’ll see detailed error messages that help us fix it.
Purpose
Starting Point: This file starts our app and tells it how to behave.
Setup: It sets up connections to the database and prepares routes for user actions.
Testing: It allows us to quickly check if the app is running correctly.


Documentation for config.py
What is config.py?
config.py is where we store all the important settings for our app. Think of it as the settings menu where we can adjust how our app works.

Key Parts
Imports:

import os: This line lets us access environment variables (like secrets and configuration settings stored outside our code).
Configuration Class:

We create a class called Config that holds all our settings. This keeps everything organized.
Database Connection:

SQLALCHEMY_DATABASE_URI: This setting tells the app where to find the database. If we don’t have a specific address, it will use a default SQLite database called neurobudget.db.
Track Modifications:

SQLALCHEMY_TRACK_MODIFICATIONS: This setting helps improve performance by turning off unnecessary tracking. It’s like saying, "I don’t need to keep track of every little change."
JWT Secret Key:

JWT_SECRET_KEY: This key is used to create secure tokens for user login. It’s pulled from environment variables for security reasons.
Debug Mode:

DEBUG: This setting decides whether to run the app in debug mode, which shows helpful error messages if something goes wrong.
Purpose
Centralized Settings: This file keeps all our important settings in one place, making it easy to manage.
Environment-Specific: We can change settings based on whether we’re developing locally or deploying the app for users.
Security: It helps keep sensitive information, like secret keys, secure by storing them outside the code.
