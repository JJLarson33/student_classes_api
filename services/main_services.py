from typing import List
from modules.school_module import Student, StudentRequest, Course


def get_student_by_id_query(student_id) -> str:
    return f'SELECT * FROM STUDENTS WHERE STUDENTID={student_id}'

def get_all_students_query() -> str:
    return 'SELECT * FROM STUDENTS'

def validate_student_request(student: StudentRequest) -> str:
    msg = ""
    if student.StudentID < 0 or student.StudentID == "":
        msg += f"Student ID can't be empty or negative.  "
    if student.Enrolled == "":
        msg += f"Enrollment must be either True or False.  "
    if student.Age < 0 or student.Age == "":
        msg += f"Age field can't be negative, empty, or zero.  "
    if student.FirstName == "":
        msg += f"First name field can't be empty.  "
    if student.LastName == "":
        msg += f"Last name field can't be empty.  "
    if student.Gender == "":
        msg += f"Gender field can't be empty.  "
    if student.Email == "":
        msg += f"Email field can't be empty.  "
    if student.Phone == "":
        msg += f"Phone field can't be empty.  "
    if student.Address == "":
        msg += f"Address field can't be empty.  "
    if student.JoinDate == "":
        msg += f"Join date field can't be empty.  "
    if not student.CourseList:
        msg += f"Course list can't be empty.  "
    return msg

def insert_new_student(new_student: StudentRequest, courses) -> str:
    return f'INSERT INTO STUDENTS (STUDENTID, ENROLLED, AGE, FIRSTNAME, LASTNAME, GENDER, EMAIL, PHONE, ADDRESS, JOINDATE, CLASSLIST) VALUES ({new_student.StudentID}, "{new_student.Enrolled}", {new_student.Age}, "{new_student.FirstName}", "{new_student.LastName}", "{new_student.Gender}", "{new_student.Email}", "{new_student.Phone}", "{new_student.Address}","{new_student.JoinDate}", "{courses}")'

def modify_student(student: StudentRequest, courses) -> str:
    return f'UPDATE STUDENTS SET ENROLLED="{student.Enrolled}", AGE={student.Age}, FIRSTNAME="{student.FirstName}", LASTNAME="{student.LastName}", GENDER="{student.Gender}", EMAIL="{student.Email}", PHONE="{student.Phone}", ADDRESS="{student.Address}", JOINDATE="{student.JoinDate}", CLASSLIST="{courses}" WHERE STUDENTID={student.StudentID}'

def get_all_tokens() -> str:
    return 'SELECT * FROM TOKENS'

def convert_all_tokens_to_list(tuples) -> list[str]:
    converted = []
    for token in tuples:
        converted.append(token[0])
    return converted

def convert_student_to_object(students, courses) -> list[Student]:
    updated_students = []
    # Once data gets here, within for loop every row becomes a tuple
    for row in students:
        # (0, 'False', '21', 'Veronica', 'Potter', 'female', 'veronicapotter@furnigeer.com', '+1 (849) 512-2231', '771 Downing Street, Tyro, Nebraska, 6696', 'Wed Feb 19 2020 07:25:47', '0,2,14,9') <- example data
        student_class_list = convert_string_to_integer_list(row[10])
        student_courses = find_student_courses(courses, student_class_list)
        updated_students.append(
            Student(StudentID=row[0], Enrolled=row[1], Age=row[2], FirstName=row[3], LastName=row[4], Gender=row[5],
                    Email=row[6], Phone=row[7], Address=row[8], JoinDate=row[9], CourseList=student_courses))
    return updated_students

def convert_string_to_integer_list(course_str) -> list[int]:
    return [int(i) for i in course_str.split(",") if i]
    #class_list = []
    # example string "0,2,14,9"
    #converted = course_str.split(",")
    #for i in converted:
    #    class_list.append(int(i))
    #return class_list

def get_all_classes_query() -> str:
    return 'SELECT * FROM CLASSES'

def convert_class_to_object(data) -> list[Course]:
    courses = []
    # Once data gets here, within for loop every row becomes a tuple
    for row in data:
        # (0, 'INFO 1003', 'Basic Programming', 'Basic programming class using Python') <- example data
        courses.append(Course(ClassID=row[0], Code=row[1], Title=row[2], Description=row[3]))
    return courses

def find_student_courses(courses, student_class_list) -> list[Course]:
    student_courses = []
    for class_id in student_class_list:
        for course in courses:
            if class_id == course.ClassID:
                student_courses.append(course)
    return student_courses

def convert_dict_list_to_string(courses) -> str:
    courses_str = ""
    for course in courses:
        courses_str += str(course.ClassID) + ","
    return courses_str
