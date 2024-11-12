from typing import List
import os.path
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from databases import Database

from modules.school_module import Student, StudentRequest, WarningMessage, ErrorMessage, error_db, error_db_no_record, \
    error_id_str, warning_id, warning_auth, error_db_record_already_exists, error_db_record_not_found

from services.main_services import get_student_by_id_query, get_all_students_query, get_all_classes_query, convert_student_to_object, \
   validate_student_request, modify_student, insert_new_student, get_all_tokens, convert_all_tokens_to_list, \
    convert_string_to_integer_list, convert_class_to_object, convert_dict_list_to_string, find_student_courses

app = FastAPI(title='Final Project',
              version="0.0.10",
              contact={'name': 'Jonah J Larson', 'email': 'jlarson3@mail.mccneb.edu'},
              description='Using Python & FastAPI to simulate an API for student/class info')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

database = Database("sqlite:///services/school.db")
tokens = []

@app.on_event("startup")
async def database_connect():
    await database.connect()
    reply = await database.fetch_all(get_all_tokens())
    print(reply)
    print(convert_all_tokens_to_list(reply))
    global tokens
    tokens = convert_all_tokens_to_list(reply)

@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.get("/student", response_model=Student, responses={200: {"model": Student}, 409:{"model": WarningMessage}, 400: {"model": ErrorMessage}, 401: {"model": WarningMessage}})
async def get_student(request: Request, student_id = 'NO VALUE'):

    if request.headers['Authorization'] not in tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=warning_auth)

    path = './services/school.db'
    check_file = os.path.isfile(path)
    if not check_file:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_db)

    if student_id == 'NO VALUE':
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=warning_id)
    try:
        int(student_id)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_id_str)
    try:
        if int(student_id) < 0:
            raise Exception
    except:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=warning_id)
    student = await database.fetch_one(get_student_by_id_query(student_id))
    if student is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_db_no_record)

    student_class_list = convert_string_to_integer_list(student['CLASSLIST'])
    classes = await database.fetch_all(get_all_classes_query())
    courses = convert_class_to_object(classes)
    student_courses = find_student_courses(courses, student_class_list)
    return Student(StudentID=student['STUDENTID'], Enrolled=student['ENROLLED'], Age=student['AGE'], FirstName=student['FIRSTNAME'], LastName=student['LASTNAME'], Gender=student['GENDER'], Email=student['EMAIL'], Phone=student['PHONE'], Address=student['ADDRESS'], JoinDate=student['JOINDATE'], CourseList=student_courses)

@app.get("/students", response_model=List[Student], responses={200: {"model": List[Student]}, 400: {"model": ErrorMessage}, 401: {"model": WarningMessage}})
async def get_all_students(request: Request):

    if request.headers['Authorization'] not in tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=warning_auth)

    path = './services/school.db'
    check_file = os.path.isfile(path)
    if not check_file:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_db)

    students = await database.fetch_all(get_all_students_query())

    classes = await database.fetch_all(get_all_classes_query())
    courses = convert_class_to_object(classes)
    return convert_student_to_object(students, courses)


@app.post("/student/add/", response_model=str, responses={200: {"model": str}, 400: {"model": ErrorMessage}, 401: {"model": WarningMessage}})
async def add_student(student: StudentRequest, request: Request):

    if request.headers['Authorization'] not in tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=warning_auth)

    path = './services/school.db'
    check_file = os.path.isfile(path)
    if not check_file:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_db)

    validate_msg = validate_student_request(student)
    if validate_msg != "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validate_msg)

    check_student_exists = await database.fetch_one(get_student_by_id_query(student.StudentID))
    result_msg = ""
    if check_student_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_db_record_already_exists)
    if not check_student_exists:
        courses = convert_dict_list_to_string(student.CourseList)
        await database.execute(insert_new_student(student, courses))
        result_msg = "Successfully added new student."
    return result_msg

@app.post("/student/update/", response_model=str, responses={200: {"model": str}, 400: {"model": ErrorMessage}, 401: {"model": WarningMessage}})
async def update_student(student: StudentRequest, request: Request):

    if request.headers['Authorization'] not in tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=warning_auth)

    path = './services/school.db'
    check_file = os.path.isfile(path)
    if not check_file:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_db)

    validate_msg = validate_student_request(student)
    if validate_msg != "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validate_msg)

    check_student_exists = await database.fetch_one(get_student_by_id_query(student.StudentID))
    result_msg = ""
    if not check_student_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_db_record_not_found)
    if check_student_exists:
        courses = convert_dict_list_to_string(student.CourseList)
        await database.execute(modify_student(student, courses))
        result_msg = "Successfully updated student information."
    return result_msg
