# PERSON API Documentation

## Introduction

This document provides the overview of the standard formats for requests and responses, known limitations, and instructions for setting up and deploying the API locally or on a server.


## ENDPOINTS

### Create User

* URL: 'api/'
* Method: POST
* Request Format: 
json 

{"name": "Mark Essien"}

* Response Format:
    * Success(HTTP 201 Created):
json
{
    "id": 1,
    "name": "Mark Essien",
}

* Error(HTTP 400 Bad Request):
json
{
    "name": ["this field is required."]
}

### Retrieve, Update, Delete
* URL: 'api/{user_id}/'
* Method: 'GET', 'PUT', 'DELETE'
* Request Format(PUT):
json
{
    "name": "new_username"
}

* Response Format(PUT):
    *Success (HTTP 200 OK):
json
{
    "id": 1,
    "name": "new_username"
}

* Error(HTTP 400 Bad Request):
json
{
    "name": ["this field is required"]
}

* Response Format(GET):
    * Success(HTTP 200 OK):
json
{
    "id": 1,
    "name": "Mark Essien"
}

* Response Format(DELETE):
    * Succes (HTTP 204 No Content):
    (No response body)


# USAGE
### Create User

Request: 

POST /api/user/
Content-Type: application/json

{
    "name": "Mark Essien"
}

Response (Success- HTTP 201 Created):
json
{
    "id": 1,
    "name": "Mark Essien"
}

## Retrieve User

Request:

GET /api/1/

Response(Success-HTTP 200 OK):
json
{
    "id": 1,
    "name": "Mark Essien"
}

Update User

Request: 
PUT /api/user/1/
Content-Type: application/json

{
    "name": "new_username",
}

Response(Success-HTTP 200 OK):
json
{
    "id": 1,
    "name": "new_username",
}

### Delete User

Request:
DELETE /api/1/

Response(Success-HTTP 204 No Content):
(No response body)


## Known Limitations and Assumptions
* The API assumes that the 'User' model exists and has a field for name.
* Authentication and authorization are not implemented in this API.

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


Deploying this API to a production server:
1. Create an account with any hosting services of your choice
2. Follow the instructions on the hosting services to deploy this API.