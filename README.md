# student_classes_api

A final project and an exercise in creating an api that interacts with a database. 

- - - -

## Requirements
Using FastAPI along with Swagger, create an api with endpoints for getting a student by an ID, getting all students, adding a student, or updating a student.
Sqlite was used for the database, utilizing three tables. One for students, one for classes, and a third for tokens. This does not follow standards but was
allowed as part of the learning experience.

## How to Install / Run

Open the project folder with the IDE of choice for python (Pycharm recommended)
If there is no .db file, then run the database_creator.py file in the services folder first.
With the database file created, the next steps entail using CLI from the terminal of your IDE.

- - - -

The below are a few CLI commands to start the API and also to run the pytests.

### `uvicorn main_controller:app --reload` - Start FastAPI - visit localhost:8000/docs to view endpoints from Swagger

### `pytest test_main_controller.py::test_get_all_students_no_db -Wi::DeprecationWarning -s` - Example command line to run a specific py test, 'test_get_all_students_no_db' is the name of the specific test function within the test_main_controller.py file

### `pytest -Wi::DeprecationWarning -s` - This runs all the pytests, but I recommend commenting out the 'test_get_all_students_no_db' function before doing so if you are testing with the .db file.
