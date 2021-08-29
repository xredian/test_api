from sqlalchemy import Integer, String, Float
from sqlalchemy.sql.schema import Column
from src.database import Base


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    patronymic = Column(String, nullable=False)
    year_of_birth = Column(Integer, nullable=False)
    personnel_number = Column(Integer, unique=True)
    salary = Column(Float, nullable=False)
    position = Column(String, nullable=False)
    legal_entity = Column(String, nullable=False)
    structural_subdivision = Column(String, nullable=False)
