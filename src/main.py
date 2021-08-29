import sqlalchemy.exc
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Employee
from src.schemas import EmployeeCard, UpdateEmployeeCard

app = FastAPI()


@app.post("/new_employee", status_code=status.HTTP_201_CREATED)
def create(employee: EmployeeCard, db: Session = Depends(get_db)):
    """
    Creating new employee card
    """
    try:
        new_employee = Employee(
            surname=employee.surname,
            name=employee.name,
            patronymic=employee.patronymic,
            year_of_birth=employee.year_of_birth,
            personnel_number=employee.personnel_number,
            salary=employee.salary,
            position=employee.position,
            legal_entity=employee.legal_entity,
            structural_subdivision=employee.structural_subdivision
        )
        db.add(new_employee)
        db.commit()
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Duplicate key value. Employee with personnel number '
                                   f'{employee.personnel_number} already exists')
    return {
        "success": True,
        "created_id": new_employee.id,
        "personnel_number": new_employee.personnel_number
    }


@app.get('/', response_class=HTMLResponse)
def start_page():
    return """
    <html>
        <head>
            <title>Start page</title>
        </head>
        <body>
            <h1>Service with web API for handling list of employees using FastAPI</h1>
            <p>Please go to <a href="/docs">127.0.0.1:8000/docs</a> to use the service</p>
        </body>
    </html>
    """


@app.get('/employees')
def get_all_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return {"success": True,
            "employees": employees}


@app.get("/employees/{personnel_number}")
def get_by_personnel_number(personnel_number: int, db: Session = Depends(get_db)):
    """
    Get employee by personnel number
    """
    employee_pn = db.query(Employee).filter(Employee.personnel_number == personnel_number).first()
    if not employee_pn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Employee with personnel number {personnel_number} not found')
    return {"success": True,
            "personnel_number": personnel_number,
            "employee": employee_pn}


@app.get("/employees/{surname}/{name}/{patronymic}")
def get_by_fullname(surname: str, name: str, patronymic: str, db: Session = Depends(get_db)):
    employee_by_fullname = db.query(Employee).filter(Employee.surname == surname, Employee.name == name,
                                                     Employee.patronymic == patronymic).first()
    if not employee_by_fullname:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Employee with full name {surname} {name} {patronymic} not found')
    return {"success": True,
            "employee": employee_by_fullname}


@app.patch('/employees/{personnel_number}')
def update_an_employee(personnel_number: int, employee: UpdateEmployeeCard,
                       db: Session = Depends(get_db)):
    """
    Update whole or part of employee information
    """
    employee_to_update = db.query(Employee).filter(Employee.personnel_number == personnel_number)
    if not employee_to_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Employee with personnel number {personnel_number} not found')
    employee_to_update.update(employee.dict(exclude_unset=True))

    db.commit()

    return {"success": True,
            "personnel_number": personnel_number,
            "updated_fields": employee.dict(exclude_unset=True)}


@app.delete("/employee/{personnel_number}")
def delete(personnel_number: int, db: Session = Depends(get_db)):
    """
    Delete employee by personnel number
    """
    employee_to_delete = db.query(Employee).filter(Employee.personnel_number == personnel_number).first()

    if employee_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(employee_to_delete)
    db.commit()

    return {"success": True,
            "personnel_number": personnel_number,
            'deleted_employee': employee_to_delete}
