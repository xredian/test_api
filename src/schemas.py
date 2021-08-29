from datetime import datetime
from pydantic import BaseModel, validator
from typing import Optional


class EmployeeCard(BaseModel):
    surname: str
    name: str
    patronymic: str
    year_of_birth: int
    personnel_number: int
    salary: float
    position: str
    legal_entity: str
    structural_subdivision: str

    @validator('year_of_birth')
    def check_year_of_birth(cls, year):
        if year <= 1900 or year >= datetime.now().year:
            raise ValueError("Year of birth must be from 1900 to current")
        return year


class UpdateEmployeeCard(BaseModel):
    surname: Optional[str] = None
    name: Optional[str] = None
    patronymic: Optional[str] = None
    year_of_birth: Optional[int] = None
    personnel_number: Optional[int] = None
    salary: Optional[float] = None
    position: Optional[str] = None
    legal_entity: Optional[str] = None
    structural_subdivision: Optional[str] = None

    @validator('year_of_birth')
    def check_year_of_birth(cls, year):
        if year <= 1900 or year >= datetime.now().year:
            raise ValueError("Year of birth must be from 1900 to current")
        return year
