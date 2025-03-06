# ReactDjango-Journal
The React-Django Journal is a full-stack web application that allows users to create, manage, and securely store journal entries or notes. The backend is built using Django and Django REST Framework, while the frontend is developed with React. The project incorporates authentication, a RESTful API, and token-based authentication using JWT. 

This app is deployed on choreo and you can access the app by following this [link](https://7bf60455-1e53-478c-bdb8-125a9519ad28.e1-us-east-azure.choreoapps.dev).

I have developed this application by following a tutorial by tech with tim which can be found [here](https://www.youtube.com/watch?v=c-QsfbznSXI)

## To run the appliction locally:
Clone the repository and open the terminal
```
# Create new python environment
python -m venv venv

# Activate the environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
cd backend
python manage.py runserver

# To run the frontend 
cd frontend

# Install dependencies
npm install

# Start the frontend
npm run dev
```
## Features

- User Authentication: Secure login and registration using JWT (access and refresh tokens).

- Create, Read, and Delete Journal Entries: Users can create and manage their journal entries.

- Protected API Endpoints: Only authenticated users can access their own data.

- Responsive UI: Built using React components for a smooth user experience.

- Axios Interceptors: Handles authentication tokens automatically in API requests.

## What I have learnt

Object-Relational Mapping (ORM) in Django

Django uses ORM to map Python objects (models) to database tables. This allows developers to interact with the database using Python rather than raw SQL. When defining models in models.py, Django automatically generates the necessary database structure.

Serializers in Django vs. Models

Django models define the database structure, but since the API communicates using JSON, we need serializers to convert models into JSON format. DRF’s serializers.py handles this transformation, making it possible for frontend applications to consume API data.

Migrations in Django

Migrations handle database schema changes:

makemigrations: Scans for model changes and generates migration files containing SQL-like instructions.

migrate: Executes the migration files to apply changes to the actual database.

JWT Authentication with Django REST Framework

The application uses JWT (JSON Web Tokens) for authentication:

Access Tokens: Short-lived tokens (e.g., 30 minutes) used for API requests.

Refresh Tokens: Long-lived tokens (e.g., 1 day) that generate new access tokens when expired.

This ensures a secure and seamless authentication experience without requiring frequent logins.

React Components and Reusability

React’s component-based architecture allows for the creation of reusable UI elements. For example, the Form component is used for both login and registration, reducing redundant code and improving maintainability.

Handling Events in React

React provides an event object when handling user interactions. For example, e.preventDefault() is used in form submissions to prevent page reloads, ensuring a smooth single-page application experience.

Axios Request Interceptors

Axios interceptors modify outgoing requests before they are sent. This project uses an interceptor to automatically attach authentication tokens to API requests:

config is an object containing the request details (e.g., headers).

The interceptor checks for stored tokens and includes them in API requests to maintain authentication.

## Technologies Used

Backend: Django, Django REST Framework, PostgreSQL

Frontend: React, Axios, React Router

Authentication: JWT (JSON Web Tokens)

