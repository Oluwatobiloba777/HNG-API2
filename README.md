# HNG-API2
A REST API capable of CRUD operations on a person resource.

# Setting Up and Deploying the API

1. Clone the repository
2. Install the required dependencies by running:
pip install -r requirements.txt
3. Create database and apply migrations by running:
python manage.py makemigrations
python manage.py migrate
4. Run the development server:
python manage.py runserver

The API will be accessible at 'hhtp://localhost:8000/api' for POST request and 'http://localhost:8000/api/{user_id}' for GET, UPDATE and DELETE
