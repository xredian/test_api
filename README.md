# Service with web API for handling list of employees using FastAPI

To run this project, you'll need to have [Docker](https://docs.docker.com/get-docker/) installed, or connect to a database yourself modifying the connection in the codebase.

## Getting started

Set up a virtual environment for the project:  
`python3 -m venv venv`

Activate the environment:  
`source venv/bin/activate`

Install the dependencies:  
`pip install -r requirements.txt`

Run the database (if needed) using the provided Makefile command:  
`make run-db`

Run the API with Uvicorn:  
`uvicorn src.main:app --reload`

Run the database migration:  
`alembic upgrade head`

## Usage

All types of requests can be made with interactive API docs: 

`http://127.0.0.1:8000/docs`

### List all employees

**Definition**

`GET /employees`

**Hit the GET endpoint**

`curl -X 'GET' \
  'http://127.0.0.1:8000/employees' \
  -H 'accept: application/json'`

**Response**

- `200 OK` on success

```json
{
  "success": true,
  "employees": [
    {
      "legal_entity": "ИП Иванов",
      "salary": 60000,
      "year_of_birth": 1995,
      "patronymic": "Иванович",
      "surname": "Иванов",
      "structural_subdivision": "ИТ",
      "position": "Инженер",
      "personnel_number": 12345,
      "name": "Иван",
      "id": 1
    },
    {
      "legal_entity": "ИП Петров",
      "salary": 70000,
      "year_of_birth": 1990,
      "patronymic": "Петрович",
      "surname": "Петров",
      "structural_subdivision": "ИТ",
      "position": "Инженер",
      "personnel_number": 123456,
      "name": "Петр",
      "id": 1
    }
  ]
  
}
```

### Registering a new employee

**Definition**

`POST /new_employee`

**Hit the POST endpoint**

`curl -X 'POST' \
  'http://127.0.0.1:8000/new_employee' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "surname": "Иванов",
  "name": "Иван",
  "patronymic": "Иванович",
  "year_of_birth": 1995,
  "personnel_number": 12345,
  "salary": 600000,
  "position": "Инженер",
  "legal_entity": "ИП Иванов",
  "structural_subdivision": "ИТ"
}'`

**Arguments**

- `"surname":string` employees surname
- `"name":string` employees name
- `"patronymic":string` employees patronymic
- `"year_of_birth":integer` employees year of birth
- `"personnel_number":integer,unique` employees personnel number
- `"salary":float` employees salary
- `"position":string` employees position
- `"legal_entity":string` legal entity in which employee is registered
- `"structural_subdivision:string` structural subdivision to which employee belongs

**Response**

- `201 Created` on success

```json
{
  "success": true,
  "created_id": 2,
  "personnel_number": 12345
}
```

## Lookup employee info by personnel number

**Definition**

`GET /employees/<personnel_number>`

**Hit the GET endpoint**

`curl -X 'GET' \
  'http://127.0.0.1:8000/employees/12345' \
  -H 'accept: application/json'`

**Response**

- `404 Not Found` if the employee does not exist
- `200 OK` on success

```json
{
  "success": true,
  "personnel_number": 12345,
  "employee": {
    "legal_entity": "ИП Иванов",
    "salary": 60000,
    "year_of_birth": 1995,
    "patronymic": "Иванович",
    "surname": "Иванов",
    "structural_subdivision": "ИТ",
    "position": "Инженер",
    "personnel_number": 12345,
    "name": "Иван",
    "id": 1
  }
}
```

## Lookup employee info by full name

**Definition**

`GET /employees/<surname>/<name>/<patronymic>`

**Hit the GET endpoint**

`curl -X 'GET' \
  'http://127.0.0.1:8000/employees/Ivanov/Ivan/Ivanovich' \
  -H 'accept: application/json'`

**Response**

- `404 Not Found` if the employee does not exist
- `200 OK` on success

```json
{
  "success": true,
  "employee": {
    "legal_entity": "ИП Иванов",
    "salary": 60000,
    "year_of_birth": 1995,
    "patronymic": "Иванович",
    "surname": "Иванов",
    "structural_subdivision": "ИТ",
    "position": "Инженер",
    "personnel_number": 12345,
    "name": "Иван",
    "id": 1
  }
}
```

## Update employee information

**Definition**

`PATCH /employees/<personnel_number>`

**Hit the PATCH endpoint** 

`curl -X 'PATCH' \
  'http://127.0.0.1:8000/employees/858' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "salary": 65000
}'`

**Arguments**

- `"surname":string` employees surname
- `"name":string` employees name
- `"patronymic":string` employees patronymic
- `"year_of_birth":integer` employees year of birth
- `"personnel_number":integer,unique` employees personnel number
- `"salary":float` employees salary
- `"position":string` employees position
- `"legal_entity":string` legal entity in which employee is registered
- `"structural_subdivision:string` structural subdivision to which employee belongs

All arguments are optional for PATCH request

**Response**

- `404 Not Found` if the employee does not exist
- `200 OK` on success

```json
{
  "success": true,
  "personnel_number": 858,
  "updated_fields": {
    "salary": 65000
  }
}
```

## Delete an employee

**Definition**

`DELETE /employee/<personnel_number>`

**Hit the DELETE endpoint**

`curl -X 'DELETE' \
  'http://127.0.0.1:8000/employee/12345' \
  -H 'accept: application/json'`


**Response**

- `404 Not Found` if the employee does not exist
- `204 No Content` on success

```json
{
  "success": true,
  "personnel_number": 12345,
  "deleted_employee": {
    "legal_entity": "ИП Иванов",
    "salary": 600000,
    "year_of_birth": 1995,
    "patronymic": "Иванович",
    "surname": "Иванов",
    "structural_subdivision": "ИТ",
    "position": "Инженер",
    "personnel_number": 12345,
    "name": "Иван",
    "id": 2
  }
}
```
