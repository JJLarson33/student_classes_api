from fastapi.testclient import TestClient
from main_controller import app


test_client = TestClient(app)

def test_get_student_by_id():
    response = test_client.get('/student?student_id=0')
    print(f'\nStatus Code:', response.status_code)
    print(response.json())
    assert response.status_code == 200

def test_get_student_by_no_id():
    response = test_client.get('/student')
    print(f'Student ID Empty : ', response)
    assert response.status_code == 409

def test_get_student_negative_id():
    response = test_client.get('/student?student_id=-1')
    print(f'Student ID not positive : ' , response)
    assert response.status_code == 409

def test_get_student_by_bad_id():
    response = test_client.get('/student?student_id=aaaa')
    print(f'Student Not Found : ', response)
    assert response.status_code == 400

def test_get_all_students():
    response = test_client.get('/students')
    print(f'\nLength of List of Students: ', len(response.json()))
    assert len(response.json()) > 0
    assert response.status_code == 200

# this test must be run after deleting or removing the DB file to ensure it has no db file or delete the file and
# use this command line to only test this pytest function
# "pytest test_main_controller.py::test_get_all_students_no_db -Wi::DeprecationWarning -s"
def test_get_all_students_no_db():
    response = test_client.get('/students')
    print(f'No Database found : ', response)
    assert response.status_code == 400

def test_update_student():
    response = test_client.post('/student/update', json={"StudentID": 21,
                                                             "Enrolled": "true",
                                                             "Age": 10,
                                                             "FirstName": "Nothing",
                                                             "LastName": "Nothing",
                                                             "Gender": "female",
                                                             "Email": "long email string",
                                                             "Phone": "long phone number",
                                                             "Address": "long string address",
                                                             "JoinDate": "long joindate string",
                                                             "CourseList": [
                                                                 {
                                                                     "ClassID": 1,
                                                                     "Code": "info something",
                                                                     "Title": "a new title",
                                                                     "Description": "a new lengthy description",
                                                                 }
                                                               ]
                                                             })
    print(f'Student Updated : ', response.json())
    assert response.status_code == 200
    assert "Successfully updated student information." in response.json()

def test_update_student_fail_validation():
    response = test_client.post('/student/update', json={"StudentID": 21,
                                                             "Enrolled": "true",
                                                             "Age": -10,
                                                             "FirstName": "Nothing",
                                                             "LastName": "Nothing",
                                                             "Gender": "female",
                                                             "Email": "long email string",
                                                             "Phone": "long phone number",
                                                             "Address": "long string address",
                                                             "JoinDate": "long joindate string",
                                                             "CourseList": [
                                                                 {
                                                                     "ClassID": 1,
                                                                     "Code": "info something",
                                                                     "Title": "a new title",
                                                                     "Description": "a new lengthy description",
                                                                 }
                                                               ]
                                                             })
    print(f'Student Not Updated : ', response.json())
    assert response.status_code == 400
    assert response.json() == {'detail': "Age field can't be negative, empty, or zero.  "}

def test_add_student_already_exists():
    response = test_client.post('/student/add', json={"StudentID": 21,
                                                          "Enrolled": "true",
                                                          "Age": 9,
                                                          "FirstName": "Something",
                                                          "LastName": "Something",
                                                          "Gender": "male",
                                                          "Email": "blah@gmail.com",
                                                          "Phone": "830812093120",
                                                          "Address": "1209830192831 alksjdaljd street etc etc etc",
                                                          "JoinDate": "a long date string goes here",
                                                          "CourseList": [
                                                            {
                                                                "ClassID": 0,
                                                                "Code": "string",
                                                                "Title": "string",
                                                                "Description": "string"
                                                            }
                                                           ]
                                                          })
    print(f'Student not added, already exists: ' , response.json())
    assert response.status_code == 400
    assert response.json() == {'detail': 'The student ID supplied is taken, please try another.  '}

def test_add_student():
    response = test_client.post('/student/add', json={"StudentID": 35,
                                                          "Enrolled": "true",
                                                          "Age": 19,
                                                          "FirstName": "Something",
                                                          "LastName": "Something",
                                                          "Gender": "male",
                                                          "Email": "blah@gmail.com",
                                                          "Phone": "830812093120",
                                                          "Address": "1209830192831 alksjdaljd street etc etc etc",
                                                          "JoinDate": "a long date string goes here",
                                                          "CourseList": [
                                                            {
                                                                "ClassID": 0,
                                                                "Code": "string",
                                                                "Title": "string",
                                                                "Description": "string"
                                                            }
                                                           ]
                                                          })
    print(f'Student added: ' , response.json())
    assert response.status_code == 200
    assert "Successfully added new student." in response.json()

