from pydantic import BaseModel
from typing import List

class Course(BaseModel):
    ClassID: int
    Code: str
    Title: str
    Description: str

class Student(BaseModel):
    StudentID: int
    Enrolled: str
    Age: int
    FirstName: str
    LastName: str
    Gender: str
    Email: str
    Phone: str
    Address: str
    JoinDate: str
    CourseList: List[Course]

class StudentRequest(BaseModel):
    StudentID: int
    Enrolled: str
    Age: int
    FirstName: str
    LastName: str
    Gender: str
    Email: str
    Phone: str
    Address: str
    JoinDate: str
    CourseList: List[Course]

class WarningMessage(BaseModel):
    warning: str

class ErrorMessage(BaseModel):
    error: str

error_db = "No records found.  "
error_db_no_record = "Requested Student ID not found in database.  "
error_db_record_already_exists = "The student ID supplied is taken, please try another.  "
error_db_record_not_found = "The student ID supplied is not found, cannot update records.  "
error_id_str = "Invalid Student ID, must be a non-negative number.  "
warning_id = "Invalid Student ID, can't be empty or negative.  "
warning_auth = "Token not recognized. Unauthorized request.  "